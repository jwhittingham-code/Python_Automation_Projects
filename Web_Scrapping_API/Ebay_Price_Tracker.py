import bs4 as bs
import re 
#removed some imported items Im not sure I needed. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#--------------------------------------------------------------------------
#functions
#--------------------------------------------------------------------------
def roundprice(price):
    i = int(round(price))
    return i 

def additem(results):
    ilist = []
    for li in results:
        item = {}
        try:
            item_title = li.find("span", {"class":"su-styled-text primary default"})
            item_title = re.split(r'[><]',str(item_title))  
            item_title = item_title[2]    
        except:
            pass
        
        try:
            item_price = li.find("span", {"class":"su-styled-text primary bold large-1 s-card__price"})
            item_price = re.split(r'[><]',str(item_price)) 
            item_price = item_price[2].split(" ")
            item_price[1] = float(item_price[1].strip("$"))

            #NOTE: creating a list for price [0] is currency [1] is value
            
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
            item["title"] = item_title
            item["price"] = item_price
            item["link"] = item_link
            
            if item["price"] != ['None']:
                ilist.append(item)
        except:
            pass
    return ilist

def listcheapest(ilist):
    top5 = []
    for item in ilist:
        
        if len(top5) < 5:
            top5.append(item)
        elif len(top5) <= 5:
            for i in range(5):
                if item["price"] < top5[i]["price"]:
                    top5.pop(i)
                    top5.append(item)
                    break
                continue
    
    top5 = sorted(top5, key = lambda x: int(round(x["price"][1])))
    return top5

def displaylist(ilist):
    for i in ilist:
        print("")
        print(i["title"])
        print(i["price"][0]," $",i["price"][1])
        print("link: ", i["link"])
        print("")
        print("-----------------------------------------------------------------------------------")

#--------------------------------------------------------------------------
#setting link and creating scrapping driver from selenium
link = "https://www.ebay.com.au/sch/i.html?_nkw=zelda+ds&_sacat=0&_from=R40&_trksid=p4624852.m570.l1313"

driver = webdriver.Firefox()
driver.get(link)

#waiting for page to load so we can grab information. 
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"srp-results")))    

#grabbing page source, closing page then parsing source html      
body = driver.page_source
title = driver.title
driver.quit()
page_parse = bs.BeautifulSoup(body, 'html.parser')

#pulling list of search results.
results = page_parse.find("ul",{"class":"srp-results srp-list clearfix"})

#creating list of the 5 cheapest items
itemlist = listcheapest(additem(results))

#displaying results
print("driver title: ", title)
displaylist(itemlist)




