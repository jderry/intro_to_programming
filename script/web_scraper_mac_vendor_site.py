import urllib
from bs4 import BeautifulSoup
import pickle
import os

import os

home_dir = home_dir = os.path.expanduser('~')

with open(home_dir + '/pickle/hw_addr.pickle.bin', 'rb') as inFile:
    hw_addr = pickle.load(inFile)
