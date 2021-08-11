import requests
from bs4 import BeautifulSoup
from os import path 

def get_item():
    site_dir=path.join(path.dirname(__file__), 'HTMLFIles')
    source=open((path.join(site_dir,"CPUSearch.HTML")),'r')
    soup = BeautifulSoup(source,'lxml')
    name = soup.find('div',class_="item-title")
    print(name.text)

get_item()