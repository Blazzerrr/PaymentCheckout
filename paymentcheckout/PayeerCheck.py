import requests
import json
import re


class PayeerAPIException(Exception):
    """Базовый Payeer API класс исключения"""


class PayeerCheck:
    def __init__(self, PAYEER_ID, PAYEER_API_ID, PAYEER_API_KEY, PAYEER_PAY_TYPE, PAYEER_PAY_SUM, PAYEER_PAY_CURRENCY, PAYEER_PAY_COMMENT):
        self.PAYEER_ID = PAYEER_ID
        self.PAYEER_API_ID = PAYEER_API_ID
        self.PAYEER_API_KEY = PAYEER_API_KEY
        self.PAYEER_PAY_TYPE = PAYEER_PAY_TYPE
        self.PAYEER_PAY_SUM = PAYEER_PAY_SUM
        self.PAYEER_PAY_CURRENCY = PAYEER_PAY_CURRENCY
        self.PAYEER_PAY_COMMENT = PAYEER_PAY_COMMENT
        self.api_url = 'https://payeer.com/ajax/api/api.php'
        self.auth_data = {'account': self.PAYEER_ID, 'apiId': self.PAYEER_API_ID, 'apiPass': self.PAYEER_API_KEY}

    def history(self, **kwargs):
        kwargs['action'] = 'history'
        data = self.auth_data
        if kwargs:
            data.update(kwargs)
        resp = requests.post(url=self.api_url, data=data).json()
        error = resp.get('errors')
        if error:
            raise PayeerAPIException(error)
        else:
            resp = resp
        a = resp['history']

        for k, v in a.items():
            id = a[k]['id']
            date = a[k]['date']
            type = a[k]['type']
            status = a[k]['status']
            if "from" in a[k]:
                from_at = str(a[k]["from"])
            else:
                from_at = 'None'

            if "debitedAmount" in a[k]:
                debitedAmount = str(a[k]["debitedAmount"])
            else:
                debitedAmount = 'None'   

            if "debitedCurrency" in a[k]:
                debitedCurrency = str(a[k]["debitedCurrency"])
            else:
                debitedCurrency = 'None'

            if "to" in a[k]:
                to = str(a[k]["to"])
            else:
                to = 'None'

            if "creditedAmount" in a[k]:
                creditedAmount = str(a[k]["creditedAmount"])
            else:
                creditedAmount = 'None'   

            if "creditedCurrency" in a[k]:
                creditedCurrency = str(a[k]["creditedCurrency"])
            else:
                creditedCurrency = 'None'

            if "payeerFee" in a[k]:
                payeerFee = str(a[k]["payeerFee"])
            else:
                payeerFee = 'None'

            if "gateFee" in a[k]:
                gateFee = str(a[k]["gateFee"])
            else:
                gateFee = 'None'   

            if "exchangeRate" in a[k]:
                exchangeRate = str(a[k]["exchangeRate"])
            else:
                exchangeRate = 'None'

            if "comment" in a[k]:
                comment = str(a[k]["comment"])
            else:
                comment = 'None'

            if "isApi" in a[k]:
                isApi = str(a[k]["isApi"])
            else:
                isApi = 'None'

            if "paySystem" in a[k]:
                paySystem = str(a[k]["paySystem"])
            else:
                paySystem = 'None'
              
            #FULL STRING string = id + ' ' + date + ' ' + type + ' ' + status + ' ' + from_at + ' ' + debitedAmount + ' ' + debitedCurrency + ' ' + to + ' ' + creditedAmount + ' ' + creditedCurrency + ' ' + payeerFee + ' ' + gateFee + ' ' + exchangeRate + ' ' + comment + ' ' + isApi + ' ' + paySystem
            string = id + ' ' + date + ' ' + type + ' ' + creditedAmount + ' ' + creditedCurrency + ' ' + status + ' ' + comment

            find = self.PAYEER_PAY_TYPE + ' ' + self.PAYEER_PAY_SUM + ' ' + self.PAYEER_PAY_CURRENCY + ' ' + "success" + ' ' + self.PAYEER_PAY_COMMENT

            if find in string:
                respay_py = "Success"
                break
            else:
                respay_py = "Fail"

        return respay_py