# Python Payment Checkout

Payment verification for QIWI, Payeer, YooMoney, WebMoney and QIWI Virtual Bank Card

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

q = QiwiCheck.Qiwi(QIWI_TOKEN, QIWI_ACCOUNT)
r = q.result_pay(QIWI_PAY_TYPE, QIWI_PAY_SUM, QIWI_PAY_CURRENCY, QIWI_PAY_COMMENT)
print(r)
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
PAYEER_PAY_SUM = '1000' 
PAYEER_PAY_CURRENCY = 'RUB'
PAYEER_PAY_COMMENT = 'None'

p = PayeerCheck.Payeer(PAYEER_ID, PAYEER_API_ID, PAYEER_API_KEY)
r = p.result_pay(PAYEER_PAY_TYPE, PAYEER_PAY_SUM, PAYEER_PAY_CURRENCY, PAYEER_PAY_COMMENT)
print(r)
```

### YooMoney
```python
from paymentcheckout import YooMoneyCheck

#YOOMONEY CONFIG
YM_TOKEN = "410000000000000.18D37246359386E662F137F0A76A1309A70DA3S9AF9DF11068287AA94A70A45E08742F034F40221AD60BDA62DB2352656F4B4587FE50054E5A23G27FCB693F2C029A47049ED3E767A9818468ED4F9350993537CBCC7DD098D96F5823C958335BA596F3ECD711A5CE54DA20B69FP7CBB230DB8E61744BC820812C0051292B7A09" # EXAMPLE
#YOOMONEY PAY CHECK
YM_PAY_SUM = '1000'
YM_PAY_TYPE = 'in' 
YM_PAY_COMMENT = 'None'

y = YooMoneyCheck.YooMoney(YM_TOKEN)
r = y.result_pay(YM_PAY_SUM, YM_PAY_TYPE, YM_PAY_COMMENT)
print(r)
```

### WebMoney
```python
from paymentcheckout import WebMoneyCheck

#WEBMONEY CONFIG
WEBMONEY_WALLET = "R123456789000" # EXAMPLE
CRT_PATH = "/home/name/crt.pem" # EXAMPLE PATH TO CRT
KEY_PATH = "/home/name/key.pem" # EXAMPLE PATH TO KEY
#WEBMONEY PAY CHECK
WM_PAY_SUM = '1000'
WM_PAY_COMMENT = 'None'

w = WebMoneyCheck.WebMoney(WEBMONEY_WALLET, CRT_PATH, KEY_PATH)
r = w.result_pay(WM_PAY_SUM, WM_PAY_COMMENT)
print(r)
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

c = CardCheck.Card(CARD_QIWI_TOKEN, CARD_QIWI_ACCOUNT)
r = c.result_pay(CARD_PAY_SUM, CARD_PAY_CURRENCY)
print(r)
```

## Requirements
- requests 
- re
- lxml

## Donate
— QIWI: **<code>[qiwi.com/n/BLAZZZERRR](https://qiwi.com/n/BLAZZZERRR)</code>**</br>
— BTC: **<code>bc1qhajqf6k3lass7sq8y2p3jg6xav6hrnguacdgsz</code>**</br>
— ETH: **<code>0xD2F03940ec729BfDFA79a5b7a867e8F55E470b67</code>**</br>
— XRP: **<code>r3do8Bp7qfobrv5QmyBqp3PzJ2k8VQtGY8</code>**</br>
— BNB: **<code>bnb1wv357zh590hmys3z07fv56mv8uqua4cvz2p3dw</code>**</br>
— DOGE: **<code>DL1vn98EWknvSsbkFeruZYk3DhSLft8QWQ</code>**

## Author
Blazzerrr

You can contact me at Telegram
[@blazzzerrr](https://t.me/blazzzerrr) 
