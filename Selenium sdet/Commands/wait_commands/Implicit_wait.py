from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)
start=datetime.now()
driver.implicitly_wait(10)
driver.get('https://www.google.co.in/')
driver.maximize_window()
searchbox=driver.find_element(By.NAME,'q')
searchbox.send_keys('Selenium')
searchbox.submit()
driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").click()


driver.close()
end=datetime.now()
results=end-start
print(results)
