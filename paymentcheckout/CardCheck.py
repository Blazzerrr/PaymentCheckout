import requests
import json
import re

class Card:
    def __init__(self, CARD_QIWI_TOKEN, CARD_QIWI_ACCOUNT):
        self.CARD_QIWI_TOKEN = CARD_QIWI_TOKEN
        self.CARD_QIWI_ACCOUNT = CARD_QIWI_ACCOUNT
    
    def result_pay(self, CARD_PAY_SUM, CARD_PAY_CURRENCY):
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.CARD_QIWI_TOKEN
        parameters = {'rows': '10'}
        h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + self.CARD_QIWI_ACCOUNT + '/payments', params = parameters)

        req = h.json()

        for v in req["data"]:
            type = v['type']
            sum_amount = str(v['sum']['amount'])
            currency = str(v['sum']['currency'])
            currency = currency.replace('643', 'RUB')
            comment = str(v['comment'])
            status = v['status']

            if str(CARD_PAY_SUM) == str(sum_amount) and currency == CARD_PAY_CURRENCY and r'Пополнение или возврат платежа по QVC\QVP' in comment and type == 'IN' and status == 'SUCCESS':
                return True

        return False