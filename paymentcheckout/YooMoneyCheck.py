import requests

class APIException(Exception):
    pass


class FormatError(APIException):
    def __init__(self):
        super(FormatError, self).__init__()


class ScopeError(APIException):
    def __init__(self):
        super(ScopeError, self).__init__()
        

class TokenError(APIException):
    def __init__(self):
        super(TokenError, self).__init__()


class BasePayment(object):
    @classmethod
    def send_request(cls, url, headers=None, body=None):
        if not headers:
            headers = {}
        headers['User-Agent'] = "Yandex.Money/Python"

        if not body:
            body = {}
        full_url = "https://money.yandex.ru" + url
        return cls.process_result(
            requests.post(full_url, headers=headers, data=body)
        )

    @classmethod
    def process_result(cls, result):
        if result.status_code == 400:
            raise FormatError
        elif result.status_code == 401:
            raise TokenError
        elif result.status_code == 403:
            raise ScopeError
        return result.json()


class Wallet(BasePayment):
    def __init__(self, access_token):
        self.access_token = access_token

    def _send_authenticated_request(self, url, options=None):
        return self.send_request(url, {"Authorization": f"Bearer {self.access_token}"}, options)

    def account_info(self):
        return self._send_authenticated_request("/api/account-info")

    def operation_history(self, options):
        return self._send_authenticated_request("/api/operation-history",
                                                options)


class YooMoney:
    def __init__(self, YM_TOKEN):
        self.YM_TOKEN = YM_TOKEN


    def result_pay(self, YM_PAY_SUM, YM_PAY_TYPE, YM_PAY_COMMENT):
        api = Wallet(self.YM_TOKEN)
        operations = api.operation_history({"records": 10})
        operations = operations['operations']

        for operation in operations:
            amount = float(operation['amount'])
            if amount % 1 == 0:
                amount = str(int(amount))
            else:
                amount = str(amount)

            try:
                comment = str(operation['comment'])
            except:
                comment = ''

            amount_currency = str(operation['amount_currency'])
            status = str(operation['status'])
            title = str(operation['title'])
            direction = str(operation['direction'])

            if amount == str(YM_PAY_SUM) and direction == YM_PAY_TYPE and amount_currency and (YM_PAY_COMMENT in title or YM_PAY_COMMENT in comment) and status == 'success':
                return True

        return False
            
