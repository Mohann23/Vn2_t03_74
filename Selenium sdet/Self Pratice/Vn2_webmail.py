from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

serv_obj=Service('M:\Drivers\Chrome\chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('https://www.vn2solutions.com:2096/cpsess2696531394/3rdparty/roundcube/?_task=mail&_mbox=INBOX')

#userid
driver.find_element(By.NAME,"user").send_keys("mohan.n@vn2solutions.com")

#password
driver.find_element(By.NAME,"pass").send_keys("Mohan@1234")

#login
driver.find_element(By.NAME,"login").click()

#compose
driver.find_element(By.ID,"rcmbtn104").click()

#to
driver.find_element(By.XPATH,'//*[@id="compose_to"]/div/div/ul/li/input').send_keys("sriharsha.s@vn2solutions.com")

#Subject
driver.find_element(By.NAME,"_subject").send_keys("Automatic code")

#message
driver.find_element(By.ID,"composebody").send_keys("Hello Harsha anna, Ala unaru")

#send
driver.find_element(By.ID,"rcmbtn113").click()

#logout
driver.find_element(By.XPATH,'//*[@id="rcmbtn109"]').click()

driver.close()


