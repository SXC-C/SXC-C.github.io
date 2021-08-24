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

def get_item(part):
    list_product = [
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      }
      
    ]
    site_dir=path.join(path.dirname(__file__), 'HTMLFIles')
    source=open((path.join(site_dir,part)),'r')
    soup = BeautifulSoup(source,'lxml')
    name = soup.findAll('div',class_="item-title")
    price = soup.findAll('li',class_="price-current")
    img = soup.findAll('div',class_="item-img")
    i=0
    for product in list_product:
        product['name']=name[i].text[0:name[i].text.find("(")]
        product['price']=price[i].text[0:len(price[i].text)-4]
        product['image']=(img[i].find('img')).attrs['src']
        i+=1
    return json.dumps(list_product)

@app.route("/getcpu")
def get_CPU():
    return get_item('CPUSearch.html')  

@app.route("/getmotherboard")
def get_MB():
    return get_item('MotherboardSearchAMD.html')  

@app.route("/getmemory")
def get_Memory():
    return get_item('MemorySearch.html')  

@app.route("/getvideocard")
def get_VC():
    return get_item('VideocardSearch.html')  

@app.route("/getpowersupply")
def get_PS():
    return get_item('PowerSupplySearch.html') 

@app.route("/getstorage")
def get_Storage():
    return get_item('StorageSearchHD.html') 

@app.route("/getcpucooler")
def get_Cooler():
    return get_item('CoolerSearchFan.html') 

@app.route("/getcase")
def get_Case():
    return get_item('CaseSearch.html') 

@app.route("/getos")
def get_OS():
    list_product = [
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      },
      {
          'name' : 'loading...',
          'price' : 'loading..',
          'image' : 'loading...',

      }
      
    ]
    site_dir=path.join(path.dirname(__file__), 'HTMLFIles')
    source=open((path.join(site_dir,"OSSearch.html")),'r')
    soup = BeautifulSoup(source,'lxml')
    name = soup.findAll('div',class_="item-title")
    price = soup.findAll('li',class_="price-current")
    img = soup.findAll('div',class_="item-img")
    i=0
    for product in list_product:
        product['name']=name[i].text[0:name[i].text.find("(")]
        product['price']=price[i].text[0:len(price[i].text)-4]
        product['image']=(img[i].find('img')).attrs['src']
        i+=1
    return json.dumps(list_product)

app.run(host='0.0.0.0')

