from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time


serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
start=datetime.now()
driver.get('https://www.amazon.in/')
time.sleep(3)
driver.get('https://www.flipkart.com/')
time.sleep(3)
driver.back() #this will go back to amazon page
time.sleep(3)
driver.forward() #This will go to flipkart page
time.sleep(3)
driver.refresh() #this will refresh
time.sleep(3)
driver.close()
end=datetime.now()
results=end-start
print(results)
