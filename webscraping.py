import requests
from bs4 import BeautifulSoup
from os import path 
from flask import Flask
import json

app = Flask(__name__,
           static_url_path='',
           static_folder='site')

@app.route('/')
def root():
   return app.send_static_file('index.html')

@app.route("/getitem")
def get_item():
    list_product = [
      {
          'name' : 'Ryzen CPU',
          'price' : 1230,
          'image' : 'https://finance.yahoo.com/quote/GOOG?p=GOOG',

      },
      {
          'name' : 'Ryzen CPU',
          'price' : 1230,
          'image' : 'https://finance.yahoo.com/quote/GOOG?p=GOOG',

      },
      {
          'name' : 'Ryzen CPU',
          'price' : 1230,
          'image' : 'https://finance.yahoo.com/quote/GOOG?p=GOOG',

      }
  ]
    site_dir=path.join(path.dirname(__file__), 'HTMLFIles')
    source=open((path.join(site_dir,"CPUSearch.HTML")),'r')
    soup = BeautifulSoup(source,'lxml')
    name = soup.findAll('div',class_="item-title")
    price = soup.findAll('li',class_="price-current")
    i=0
    for product in list_product:
        product['name']=name[i].text
        product['price']=price[i].text
        i+=1
    return json.dumps(list_product)
    
app.run(host='0.0.0.0')
