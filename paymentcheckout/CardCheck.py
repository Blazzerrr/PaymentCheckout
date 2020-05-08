import requests
import json
import re

class CardCheck:
    def __init__(self, CARD_QIWI_TOKEN, CARD_QIWI_ACCOUNT, CARD_PAY_SUM, CARD_PAY_CURRENCY):
        self.CARD_QIWI_TOKEN = CARD_QIWI_TOKEN
        self.CARD_QIWI_ACCOUNT = CARD_QIWI_ACCOUNT
        self.CARD_PAY_SUM = CARD_PAY_SUM
        self.CARD_PAY_CURRENCY = CARD_PAY_CURRENCY
    
    def card_history(self):
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.CARD_QIWI_TOKEN
        parameters = {'rows': '5'}
        h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ self.CARD_QIWI_ACCOUNT +'/payments', params = parameters)
        req = json.loads(h.text)

        for v in req["data"]:
            txnId = str(v['txnId'])
            date = v['date']
            date = date.replace(date[10], ' ')
            date = date.replace(date[19], ' ')
            type = v['type']
            sum_amount = str(v['sum']['amount'])
            sum_currency = str(v['sum']['currency'])
            sum_currency = sum_currency.replace('643', 'RUB')
            comment = str(v['comment'])
            status = v['status']
            string = txnId + ' ' + date + ' ' + type + ' ' + sum_amount + ' ' + sum_currency + ' ' + status + ' ' + comment
            find = self.CARD_PAY_SUM + ' ' + self.CARD_PAY_CURRENCY + ' ' + 'SUCCESS' + ' ' + 'Пополнение или возврат платежа по QVC'

            
            if find in string:
                respay_card = "Success"
                break
            else:
                respay_card = "Fail"
                
        return respay_card 
