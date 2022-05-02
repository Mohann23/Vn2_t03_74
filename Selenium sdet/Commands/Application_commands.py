from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)
start=datetime.now()
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
driver.find_element(By.ID, 'ap_email').send_keys('mohan444a3@gmail.com')
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.ID, 'ap_password').send_keys('Mohan1999')
driver.find_element(By.ID,  'signInSubmit').click()
print(driver.title)
print(driver.current_url)
#driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('laptops')
#driver.find_element(By.ID, 'nav-search-submit-button').click()
#driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span').click()

#time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="nav-hamburger-menu"]/i').click()
driver.find_element(By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[30]/a').click()
#we need to change the xpath of above line every time
print(driver.title)
time.sleep(5)
#print(driver.page_source)   # unwanted sollu will some
driver.close()
end=datetime.now()
print('Time taken for the program to complete is: ',end-start)

