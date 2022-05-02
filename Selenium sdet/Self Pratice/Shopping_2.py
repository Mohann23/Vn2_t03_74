"""Application opens and login to its main page
It goes and select the t-shirts
it opens the t-shirt
quanity----2
colour ---Blue
screenshot will be taken of the price and everything
and proceed with the checkout
and payment will be with check
and the last it prints the total in console and
closes the application
"""

import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

from selenium.webdriver.support.select import Select

serv_obj=Service('M:\Drivers\Chrome\chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

#email
driver.find_element(By.ID,"email").send_keys("Mohan444a3@gmail.com")

#password
driver.find_element(By.ID,"passwd").send_keys("Mohan123")

#signIn
driver.find_element(By.ID,"SubmitLogin").click()

#t-Shirts
driver.find_element(By.XPATH,'//*[@id="block_top_menu"]/ul/li[3]/a').click()

#select t-shirt
driver.find_element(By.XPATH,'//*[@id="center_column"]/ul/li/div/div[2]/h5/a').click()

#click photo
driver.find_element(By.XPATH,'//*[@id="bigpic"]').click()

#takeing Screenshot
driver.save_screenshot("screenshot#"+str(random.randint(1,101))+".png")

#close
driver.find_element(By.XPATH,'//*[@id="product"]/div[2]/div/a').click()

#Qantity
driver.find_element(By.ID,"quantity_wanted").clear()
driver.find_element(By.ID,"quantity_wanted").send_keys("2")

#size
sizes=driver.find_element(By.ID,"group_1")
size=Select(sizes)
size.select_by_visible_text("L")

#colour##
driver.find_element(By.NAME,"Blue").click()

#Add to cart
driver.find_element(By.XPATH,"//span[normalize-space()='Add to cart']").click()

#Proceed to checkout
driver.find_element(By.XPATH,'//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span').click()

#total
total=driver.find_element(By.ID,"total_price_container")
print("Total bill: ",total.text)

#Proceed to check out_1
driver.find_element(By.XPATH,'//*[@id="center_column"]/p[2]/a[1]/span').click()

#proceed to check out_2
driver.find_element(By.XPATH,'//*[@id="center_column"]/form/p/button/span').click()

#Check box of t&m
driver.find_element(By.NAME,"cgv").click()

#Proceed to Checkout 3
driver.find_element(By.XPATH,'//*[@id="form"]/p/button/span').click()

#Pay by check
driver.find_element(By.XPATH,'//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a').click()

#Confirm order
driver.find_element(By.XPATH,'//*[@id="cart_navigation"]/button/span').click()

driver.quit()

