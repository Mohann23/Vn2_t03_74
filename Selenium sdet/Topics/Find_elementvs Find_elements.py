from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time

serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/')

##Find_element()
'''
#1)locator matching with the single web element
elements=driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
elements.send_keys('mobiles')
'''
'''
#2)Locator matching with the multiple web elements
elements=driver.find_element(By.XPATH,'/html/body/div[6]/div[4]/div[1]/div[1]/ul/li[1]')
print(elements.text) #prints first link from the footer sitemap
'''
'''
#3)element not available then throw Nosuchelement exception
elements=driver.find_element(By.LINK_TEXT,"Log ")
elements.click()
#In this case we get error
'''
##Find_elements()
'''
#1)locator matching with the single web element
elements=driver.find_elements(By.XPATH,'//*[@id="small-searchterms"]')
print(len(elements))
print(elements[0].send_keys('Mobiles'))
'''
#ask kiran
'''
#2)Locator matching with the multiple web elements
elements=driver.find_elements(By.XPATH,'/html/body/div[6]/div[4]/div[1]')
print(len(elements))
print(elements[0].text)
'''

'''
#3)element not available - 0
elements=driver.find_elements(By.LINK_TEXT,"Log ")
print(len(elements)) # no error will be given
'''

