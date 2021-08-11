from bs4 import BeautifulSoup
from flask import Flask
from os import path
import json 
import random
import requests

app = Flask(__name__,
           static_url_path='',
           static_folder='static')

@app.route('/')
def root():
   return app.send_static_file('index.html')

@app.route("/getitem")
def get_item():
    site_dir=path.join(path.dirname(__file__), 'HTMLFIles')
    source=open((path.join(site_dir,"CPUSearch.HTML")),'r')
    soup = BeautifulSoup(source,'lxml')
    name = soup.find('div',class_="item-title")
    print(name.text)

    return json.dumps(name.text)


app.run(host='0.0.0.0')