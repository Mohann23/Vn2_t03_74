from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from datetime import datetime

#When ever you do this better change the email id and mobile number

serv_obj=Service("M:\Drivers\Chrome\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://automationpractice.com/index.php")
driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()

#Register
#Enter email
driver.find_element(By.ID,"email_create").send_keys("Mohan44a3@gmail.com")
driver.find_element(By.XPATH,'//*[@id="SubmitCreate"]/span').click()     #To click create an account
'''
#Select Gender
driver.find_element(By.XPATH,'//*[@id="account-creation_form"]/div[1]/div[1]/div[1]').submit()
'''
#First name
driver.find_element(By.ID,"customer_firstname").send_keys("Mohan")

#lastname
driver.find_element(By.ID,"customer_lastname").send_keys("Narayana")

#password
driver.find_element(By.NAME,"passwd").send_keys("Mohan123")

#date
day=driver.find_element(By.ID,"days")
date=Select(day)
date.select_by_value("23")

#months
months=driver.find_element(By.NAME,"months")
month=Select(months)
month.select_by_visible_text("August ")

#year
years=driver.find_element(By.ID,"years")
year=Select(years)
year.select_by_visible_text("1999  ")

#newsletter checkbox
driver.find_element(By.NAME,"newsletter").click()

#special offers checkbox
driver.find_element(By.NAME,"optin").click()

#address
driver.find_element(By.NAME,"address1").send_keys("Unispace123")

#state
states=driver.find_element(By.NAME,"id_state")
state=Select(states)
state.select_by_visible_text("California")

#city
driver.find_element(By.NAME,"city").send_keys("Bangalore")

#postcode
driver.find_element(By.ID,"postcode").send_keys("00000")

#mobile Number
driver.find_element(By.NAME,"phone_mobile").send_keys("0223456789")

#alias
alias=driver.find_element(By.NAME,"alias")
alias.clear()
alias.send_keys("Mona")

#register
driver.find_element(By.XPATH,'//*[@id="submitAccount"]/span').click()


















