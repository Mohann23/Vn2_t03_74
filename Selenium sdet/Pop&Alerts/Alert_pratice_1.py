from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time

serv_obj=Service('M:\Drivers\Chrome\chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get('https://demoqa.com/alerts')

driver.find_element(By.ID,"confirmButton").click()
alert_window=driver.switch_to.alert
print(alert_window.text)
alert_window.accept()
driver.close()


