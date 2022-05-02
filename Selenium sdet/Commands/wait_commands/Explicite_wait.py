
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)


my_wait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,
                                                    Exception,
                                                    ElementNotSelectableException])


driver.get('https://www.google.co.in/')
driver.maximize_window()
searchbox=driver.find_element(By.NAME,'q')

searchbox.send_keys('Selenium')
searchbox.submit()
searchlink=my_wait.until(EC.presence_of_element_located(By.XPATH,"//h3[normalize-space()='Selenium']"))
searchlink.click()

driver.quit()
###What ever we do we are getting some kind of error in this
##better avoid this model
