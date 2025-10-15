import bs4 as bs
import requests
import numpy as np
import csv
from datetime import datetime

#print(np.__version__)

link = "https://www.ebay.com.au/sch/i.html?_nkw=zelda+ds&_sacat=0&_from=R40&_trksid=p4624852.m570.l1313"

r = requests.get(link)
page_parse = bs.BeautifulSoup(r.text, 'html.parser')

#print(page_parse)

results = page_parse.find("body")

print(results)