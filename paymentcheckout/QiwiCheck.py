import requests
import json
import re

class Qiwi:
    def __init__(self, QIWI_TOKEN, QIWI_ACCOUNT):
        self.QIWI_TOKEN = QIWI_TOKEN
        self.QIWI_ACCOUNT = QIWI_ACCOUNT
    
    def result_pay(self, QIWI_PAY_TYPE, QIWI_PAY_SUM, QIWI_PAY_CURRENCY, QIWI_PAY_COMMENT):
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.QIWI_TOKEN
        parameters = {'rows': '10'}
        h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + self.QIWI_ACCOUNT + '/payments', params = parameters)

        req = h.json()


        for v in req["data"]:
            type = v['type']
            sum_amount = str(v['sum']['amount'])
            currency = str(v['sum']['currency'])
            currency = currency.replace('643', 'RUB')
            comment = str(v['comment'])
            status = str(v['status'])

            if str(QIWI_PAY_SUM) == str(sum_amount) and currency == QIWI_PAY_CURRENCY and QIWI_PAY_COMMENT in comment and type == QIWI_PAY_TYPE and status == 'SUCCESS':
                return True

        return False

