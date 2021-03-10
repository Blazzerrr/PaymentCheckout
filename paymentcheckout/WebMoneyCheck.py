import os
import time
import uuid
import xmltodict
import ssl
import requests as r
from lxml import etree
from pprint import pprint, pformat
from datetime import datetime, timedelta
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.exceptions import SSLError
from requests.packages.urllib3.exceptions import InsecureRequestWarning

r.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Ssl3HttpAdapter(HTTPAdapter):

    """Transport adapter" that allows us to use SSLv3."""

    def init_poolmanager(self, connections, maxsize, block=False):

        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_SSLv23)


class AuthInterface(object):

    """
    Интерфейс аунтефикации
    """

    def wrap_request(self, request_params):
        """

        """
        return request_params

    def wrap_body_tree(self, tree):
        """

        """
        return tree

    def get_url_by_name(self, name):
        raise 'NotImplemented'


class WMLightAuthInterface(AuthInterface):

    def __init__(self, pub_cert, priv_key=None):
        if not os.path.exists(pub_cert):
            raise ValueError("Incorrect path to pub certificate")
        if priv_key and not os.path.exists(priv_key):
            raise ValueError("Incorrect path to private key")

        self.cert = os.path.abspath(
            pub_cert) if priv_key is None else (os.path.abspath(pub_cert),
                                                os.path.abspath(priv_key))

    def wrap_request(self, request_params):
        request_params.update({"cert": self.cert})
        return request_params

    def get_url_by_name(self, name):
        if name == "FindWMPurseNew":
            return "https://w3s.wmtransfer.com/asp/XMLFindWMPurseCertNew.asp"
        
        return f"https://w3s.wmtransfer.com/asp/XML{name}Cert.asp"

class ApiInterface(object):
    API_METADATA = {"FindWMPurseNew": {"root_name": "testwmpurse",
                                       "aliases": ["x8"]},
                    "Purses": {"root_name": "getpurses",
                               "aliases": ["x9"],
                               "response_name": "purses"},
                    "Invoice": {"root_name": "invoice",
                                "aliases": ["x1"]},
                    "Trans": {"root_name": "trans",
                              "aliases": ["x2"],
                              "response_name": "operation"},
                    "Operations": {"root_name": "getoperations",
                                   "aliases": ["x3"],
                                   "response_name": "operations"},
                    "OutInvoices": {"root_name": "getoutinvoices",
                                    "aliases": ["x4"],
                                    "response_name": "outinvoices"},
                    "FinishProtect": {"root_name": "finishprotect",
                                      "aliases": ["x5"],
                                      "response_name": "operation"},
                    "SendMsg": {"root_name": "message",
                                "aliases": ["x6"]},
                    "ClassicAuth": {"root_name": "testsign",
                                    "aliases": ["x7"]},
                    "InInvoices": {"root_name": "getininvoices",
                                   "aliases": ["x10"],
                                   "response_name": "ininvoices"}}

    def __init__(self, authenticationStrategy):
        self.authStrategy = authenticationStrategy

    def _check_params(self, params):
        for key in params:
            assert key in self.API_METADATA

    def _get_root_name_by_interface_name(self, interface_name):
        assert interface_name in self.API_METADATA, "Incorrect interface name: %s" % interface_name
        return self.API_METADATA[interface_name]["root_name"]

    def _create_xml_request_params(self, interface_name, params):
        root_name = self._get_root_name_by_interface_name(interface_name)
        tree = etree.Element(root_name)
        for key, value in params.items():
            subelement = etree.Element(key)
            subelement.text = value
            tree.append(subelement)

        return tree

    def _create_request(self, interface, **kwargs):
        request_params = {
            "url": self.authStrategy.get_url_by_name(interface), "verify": False}

        request_params = self.authStrategy.wrap_request(request_params)

        return request_params

    def _create_body(self, interface, **params):
        tree = etree.Element("w3s.request")

        reqn = params.pop("reqn", None)
        _ = etree.Element("reqn")

        if reqn:
            _.text = str(int(reqn))
        else:
            _.text = ""

        tree.append(_)

        tree.append(self._create_xml_request_params(interface, params))

        tree = self.authStrategy.wrap_body_tree(tree)

        return etree.tostring(tree)

    def _make_request(self, interface, **params):
        request_params = self._create_request(interface, **params)
        body = self._create_body(interface, **params)

        request_params.update({"data": body})

        s = r.Session()
        a = Ssl3HttpAdapter(max_retries=3)
        s.mount('https://', a)

        response = s.get(**request_params)

        if response.status_code != 200:
            print("Something bad:")
            print("Request status code:", response.status_code)
            print("Response:")
            print(response.text)
            exit(1)

        out = xmltodict.parse(response.text, encoding='utf-8')["w3s.response"]
        return out

    def __getattribute__(self, name):
        if name in ApiInterface.API_METADATA.keys():
            def _callback(**params):
                return self._make_request(name, **params)

            return _callback

        for key, aliases in ApiInterface.API_METADATA.items():
            aliases = aliases["aliases"]
            if name.lower() in aliases:
                def _callback(**params):
                    return self._make_request(key, **params)
                return _callback

        return object.__getattribute__(self, name)


class WebMoney:
    def __init__(self, WEBMONEY_WALLET, CRT_PATH, KEY_PATH):
        self.WEBMONEY_WALLET = WEBMONEY_WALLET 
        self.CRT_PATH = CRT_PATH
        self.KEY_PATH = KEY_PATH


    def result_pay(self, WM_PAY_SUM, WM_PAY_COMMENT):
        api = ApiInterface(WMLightAuthInterface(self.CRT_PATH, self.KEY_PATH))

        datefinish = datetime.now()
        datestart = datefinish - timedelta(hours=24) 

        datestart = datestart.strftime("%Y%m%d %H:%M:%S")
        datefinish = datefinish.strftime("%Y%m%d %H:%M:%S")

        res = api.x3(purse=self.WEBMONEY_WALLET, datestart=datestart, datefinish=datefinish, reqn=int(time.time()))

        def ordereddict_to_dict(value):
            for k, v in value.items():
                if isinstance(v, dict):
                    value[k] = ordereddict_to_dict(v)
            return dict(value)

        try:
            operations = res['operations']['operation']
        except:
            return False

        for operation in operations:
            operation = ordereddict_to_dict(operation)
            amount = operation['amount']
            opertype = operation['opertype']
            pursedest = operation['pursedest']
            desc = operation['desc'].encode('iso-8859-1').decode('windows-1251')

            if amount == str(WM_PAY_SUM) and opertype == '0' and pursedest == self.WEBMONEY_WALLET and WM_PAY_COMMENT in desc:
                return True
            
        return False

        
