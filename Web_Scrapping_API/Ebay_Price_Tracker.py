import bs4 as bs
#removed some imported items Im not sure I needed. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



link = "https://www.ebay.com.au/sch/i.html?_nkw=zelda+ds&_sacat=0&_from=R40&_trksid=p4624852.m570.l1313"


driver = webdriver.Chrome()
driver.get(link)
#setting title to see whats loaded
title = driver.title
print("driver title: ", title)

#waiting for page to load so we can grab information. 
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"srp-results")))    

#grabbing page source, closing page then parsing source html      
body = driver.page_source
driver.quit()
page_parse = bs.BeautifulSoup(body, 'html.parser')

#Setting the title a 2nd time as a method to check if the expected HTML has loaded
title = driver.title
print("driver title: ", title)

#currently just testing one piece of data before building out rest of app. 
results = page_parse.find("span",{"class":"su-styled-text primary bold large-1 s-card__price"})
print(results)

