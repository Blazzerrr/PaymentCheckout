import requests
import json
import re

class QiwiCheck:
    def __init__(self, QIWI_TOKEN, QIWI_ACCOUNT, QIWI_PAY_TYPE, QIWI_PAY_SUM, QIWI_PAY_CURRENCY, QIWI_PAY_COMMENT):
        self.QIWI_TOKEN = QIWI_TOKEN
        self.QIWI_ACCOUNT = QIWI_ACCOUNT
        self.QIWI_PAY_TYPE = QIWI_PAY_TYPE
        self.QIWI_PAY_SUM = QIWI_PAY_SUM
        self.QIWI_PAY_CURRENCY = QIWI_PAY_CURRENCY
        self.QIWI_PAY_COMMENT = QIWI_PAY_COMMENT
    
    def qiwi_history(self):
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + self.QIWI_TOKEN
        parameters = {'rows': '5'}
        h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+ self.QIWI_ACCOUNT +'/payments', params = parameters)
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
            find = self.QIWI_PAY_TYPE + ' ' + self.QIWI_PAY_SUM + ' ' + self.QIWI_PAY_CURRENCY + ' ' + 'SUCCESS' + ' ' + self.QIWI_PAY_COMMENT

            
            if find in string:
                respay_qiwi = "Success"
                break
            else:
                respay_qiwi = "Fail"

        return respay_qiwi  
