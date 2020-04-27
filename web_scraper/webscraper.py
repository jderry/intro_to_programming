# coding: utf-8
import urllib
from bs4 import BeautifulSoup
import pickle

r = urllib.request.urlopen('http://www.macvendors.com').read()


with urllib.request.urlopen('http://www.coffer.com/mac_find/?string=ec3091') as response:
    html = response.read()

##### the web scraper #####

with open('hw_addr.pickle.bin', 'rb') as handle:
      hw_addr = pickle.load(handle)

nwAppHW_addr = dict()
for address in hw_addr:
    http = 'http://www.coffer.com/mac_find/?string=' + address
    with urllib.request.urlopen(http) as response:
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        letters = soup.find_all("td", class_="table2")
        if letters:
            nwAppHW_addr[address] = letters[1].a.string.strip().lower()

##### the web scraper #####
#
##### pickling and unpickling python collections #####
with open('hw_addr.pickle.bin', 'wb') as handle:
    pickle.dump(hw_addr, handle)

with open('hw_addr.pickle.bin', 'rb') as handle:
    hw_addr = pickle.load(handle)
##### pickling and unpickling python collections #####  
