from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
email_box=driver.find_element(By.ID,"Email")
email_box.clear()
email_box.send_keys('admin@yourstore.com')
print("Results of text:",email_box.text) #prints nothing bcz there is no inner text.
print("Results of get_attribute()",email_box.get_attribute("value"))


driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys('admin')

driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
driver.quit()