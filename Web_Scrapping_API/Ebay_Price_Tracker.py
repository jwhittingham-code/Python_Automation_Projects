import bs4 as bs
import re 
#removed some imported items Im not sure I needed. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



link = "https://www.ebay.com.au/sch/i.html?_nkw=zelda+ds&_sacat=0&_from=R40&_trksid=p4624852.m570.l1313"


driver = webdriver.Firefox()
driver.get(link)
#setting title to see whats loaded

#waiting for page to load so we can grab information. 
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"srp-results")))    

#grabbing page source, closing page then parsing source html      
body = driver.page_source
title = driver.title
driver.quit()
page_parse = bs.BeautifulSoup(body, 'html.parser')

#Setting the title a 2nd time as a method to check if the expected HTML has loaded

print("driver title: ", title)

#currently just testing one piece of data before building out rest of app. 
results = page_parse.find("ul",{"class":"srp-results srp-list clearfix"})

for li in results:
    try:
        item_title = li.find("span", {"class":"su-styled-text primary default"})
        item_title = re.split(r'[><]',str(item_title))  
        item_title = item_title[2]    
    except:
        pass
    
    try:
        item_price = li.find("span", {"class":"su-styled-text primary bold large-1 s-card__price"})
        item_price = re.split(r'[><]',str(item_price)) 
        item_price = item_price[2]
         
    except:
        pass

    try:
        item_link = li.find("a", {"class":"su-link"})
        item_link = re.split(r'[><]',str(item_link))  
        item_link = item_link[1].split('"')
        item_link = item_link[41]
    except:
        pass

    try:
        print(item_title)
        print(item_price)
        print(item_link)
        # print("list length", len(item_link))

    except:
        pass



