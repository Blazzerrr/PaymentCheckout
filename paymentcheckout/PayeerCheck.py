import requests
import json
import re


class Payeer:
    def __init__(self, PAYEER_ID, PAYEER_API_ID, PAYEER_API_KEY):
        self.PAYEER_ID = PAYEER_ID
        self.PAYEER_API_ID = PAYEER_API_ID
        self.PAYEER_API_KEY = PAYEER_API_KEY

    def result_pay(self, PAYEER_PAY_TYPE, PAYEER_PAY_SUM, PAYEER_PAY_CURRENCY, PAYEER_PAY_COMMENT, **kwargs):
        api_url = 'https://payeer.com/ajax/api/api.php'
        auth_data = {'account': self.PAYEER_ID, 'apiId': self.PAYEER_API_ID, 'apiPass': self.PAYEER_API_KEY}

        kwargs['action'] = 'history'
        kwargs['count'] = '10'
        data = auth_data
        if kwargs:
            data.update(kwargs)
        resp = requests.post(url=api_url, data=data).json()

        error = resp.get('errors')
        if error:
            print(error)

        else:
            resp = resp

        a = resp['history']

        for k, _ in a.items():
            type = a[k]['type']
            status = a[k]['status']

            if "creditedAmount" in a[k]:
                creditedAmount = float(a[k]["creditedAmount"])
                if creditedAmount % 1 == 0:
                    creditedAmount = str(int(creditedAmount))
                else:
                    creditedAmount = str(creditedAmount)
            else:
                creditedAmount = 'None'   

            if "creditedCurrency" in a[k]:
                creditedCurrency = str(a[k]["creditedCurrency"])
            else:
                creditedCurrency = 'None'

            if "creditedCurrency" in a[k]:
                creditedCurrency = str(a[k]["creditedCurrency"])
            else:
                creditedCurrency = 'None'

            if "comment" in a[k]:
                comment = str(a[k]["comment"])
            else:
                comment = 'None'

            if type == PAYEER_PAY_TYPE and creditedAmount == str(PAYEER_PAY_SUM) and creditedCurrency == PAYEER_PAY_CURRENCY and PAYEER_PAY_COMMENT in comment and status == 'success':
                return True

        return False

