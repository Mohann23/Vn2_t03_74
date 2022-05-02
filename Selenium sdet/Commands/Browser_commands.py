from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)

start=datetime.now()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
#time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(5)
#driver.close() #closes only one tab
driver.quit() #closes the whole application
end=datetime.now()
print(end-start)

