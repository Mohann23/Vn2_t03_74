from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window() #To maximize screen

#open nopcommerce.com
driver.get('https://demo.nopcommerce.com/')

'''
#click on the link of Digital downloads
driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[4]/a').click()
#driver.find_element(By.LINK_TEXT,'Digital downloads').submit()
#driver.find_element(By.PARTIAL_LINK_TEXT,'Digital ').click()
#Ask kiran When ever i use link_text it is not executing properly
'''
'''
#1.find no of links in webpage
links=driver.find_elements(By.TAG_NAME,'a')
#We can even use xpath by giving '//a'
#links=driver.find_elements(By.XPATH,'//a')
print("Total links: ",len(links))
for link in links:
    print(link.text)
'''
#driver.quit()




























