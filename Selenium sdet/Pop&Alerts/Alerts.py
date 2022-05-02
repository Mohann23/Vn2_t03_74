import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service('M:\Drivers\Chrome\chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

#opern the Internet hukk_upp application
driver.get("https://demoqa.com/alerts")

#opens alert window
driver.find_element(By.ID,'promtButton').click()
time.sleep(5)

#To access the alert window we need to use this keyword
alert_window=driver.switch_to.alert
print(alert_window.text)  #print the text on the alert window
time.sleep(5)
alert_window.send_keys("Mohan") #sending words in space

alert_window.accept()  #To click ok
#alert_window.dismiss() #to click cancel









