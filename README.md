# Python Payment Checkout

Payment verification for QIWI, Payeer and QIWI Virtual Bank Card

## Installations
```
pip install paymentcheckout
```

## How to take payments on Bank Card

Register at https://qiwi.com/cards and get a virtual bank card in the Cards section

## How to use Payment Checkout
### QIWI
```python
from paymentcheckout import QiwiCheck

#QIWI CONFIG
QIWI_TOKEN = "1217163fba39a7gbzgf0527aoi7ef6er" # EXAMPLE
QIWI_ACCOUNT = '79990001234' # EXAMPLE
#QIWI PAY CHECK
QIWI_PAY_TYPE = 'IN' # IN / OUT
QIWI_PAY_SUM = '1000'
QIWI_PAY_CURRENCY = 'RUB'
QIWI_PAY_COMMENT = 'None'
q = QiwiCheck.QiwiCheck(QIWI_TOKEN, QIWI_ACCOUNT, QIWI_PAY_TYPE, QIWI_PAY_SUM, QIWI_PAY_CURRENCY, QIWI_PAY_COMMENT)
result_pay_qiwi = q.qiwi_history()
print(result_pay_qiwi)
```

### Payeer
```python
from paymentcheckout import PayeerCheck

#PAYEER CONFIG
PAYEER_ID = 'P12345678' # EXAMPLE 
PAYEER_API_ID = '999999999' # EXAMPLE 
PAYEER_API_KEY = 'B1sdboapyQSw0RAw' # EXAMPLE
#PAYEER PAY CHECK
PAYEER_PAY_TYPE = 'deposit' #deposit / transfer / withdrawal / sci
PAYEER_PAY_SUM = '1000.00' 
PAYEER_PAY_CURRENCY = 'RUB'
PAYEER_PAY_COMMENT = 'None'
p = PayeerCheck.PayeerCheck(PAYEER_ID, PAYEER_API_ID, PAYEER_API_KEY, PAYEER_PAY_TYPE, PAYEER_PAY_SUM, PAYEER_PAY_CURRENCY, PAYEER_PAY_COMMENT)
result_pay_payeer = p.history()
print(result_pay_payeer)
```

### Card QIWI
```python
from paymentcheckout import CardCheck

#CARD CONFIG
CARD_QIWI_TOKEN = "1217163fba39a7gbzgf0527aoi7ef6er" # EXAMPLE
CARD_QIWI_ACCOUNT = '79990001234' # EXAMPLE
#CARD PAY CHECK
CARD_PAY_SUM = '1000'
CARD_PAY_CURRENCY = 'RUB'
c = CardCheck.CardCheck(CARD_QIWI_TOKEN, CARD_QIWI_ACCOUNT, CARD_PAY_SUM, CARD_PAY_CURRENCY)
result_pay_card = c.card_history()
print(result_pay_card)
```

## Requirements
- requests 
- re

## Author
Blazzerrr

You can contact me at Telegram
[@blazzzerrr](https://t.me/blazzzerrr) 
