import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

URL = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey={API_KEY}'

URL1 = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey={API_KEY}'

r = requests.get(URL)
r1 = requests.get(URL1)

data = r.json()
data1 = r1.json()

exrate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

lup = data['Realtime Currency Exchange Rate']['6. Last Refreshed']

bp =  data['Realtime Currency Exchange Rate']['8. Bid Price']

ap =  data['Realtime Currency Exchange Rate']['9. Ask Price']

print("----- Currency Exchange Rate from Bitcoin to Chinese Yuan -----","\n")

print("Exchange Rate - ",exrate,"\n")

print("Bid price - ",bp,"\n")

print("Ask price - ",ap,"\n")

print("Last updated - ",lup,"\n")

print("--------------------------------------------------------------------------------------------\n")

exrate1 = data1['Realtime Currency Exchange Rate']['5. Exchange Rate']

lup1 = data1['Realtime Currency Exchange Rate']['6. Last Refreshed']

bp1 =  data1['Realtime Currency Exchange Rate']['8. Bid Price']

ap1 =  data1['Realtime Currency Exchange Rate']['9. Ask Price']

print("----- Currency Exchange Rate from US Dollar to Japanese Yen -----","\n")

print("Exchange Rate - ",exrate1,"\n")

print("Bid price - ",bp1,"\n")

print("Ask price - ",ap1,"\n")

print("Last updated - ",lup1,"\n")
