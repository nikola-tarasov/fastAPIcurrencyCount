from fastapi import FastAPI
import requests
from apikey import API_KEY


app = FastAPI()


# link = f"http://api.currencylayer.com/live?access_key={API_KEY}&currencies=RUB"
# r = requests.get(link)
# s = r["quotes"]["RUB"]

# link = f"http://api.currencylayer.com/live?access_key={API_KEY}&currencies=RUB"
# r = requests.get(link)
# # print(r.status_code)
# # print(r.json())
# s = r["quotes"]["RUB"]



usd = {"USD": 99}
euro = {"EURO": 110}
usdeuro = {"USD": 0.93}
eurousd = {"EURO": 1.01}


# получение валюты 
@app.get("/{currency}")
def read_cyrrency(currency: str):
        link = f"http://api.currencylayer.com/live?access_key={API_KEY}&currencies=RUB"
        r = requests.get(link)
        g = r.json()
        l = g['quotes']['USDRUB']
        usd["USD"] = l
        if "USD" in currency:
            return usd
        if "EURO" in currency:
            return euro
        
# получение доллара и евро курс
@app.get("/{currency}/{count}")
def read_count(currency: str, count: int):
     if "USD" in currency:
          a = usd["USD"] * int(count)
          return {"USD": a}
     elif "EURO" in currency:
          b = euro["EURO"] * int(count)
          return {"EURO": b}
     
@app.get("/{currency}/{to}/{count}")
def read_count(currency: str, to: str, count: int):

     if currency == "USD" and to == "EURO":
          c = usdeuro["USD"] * count
          return {"USDEURO": c}
     elif currency == "EURO" and to == "USD":
          d = eurousd["EURO"] * count
          return {"EUROUSD": d}

     

        


