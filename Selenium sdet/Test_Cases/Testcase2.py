import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("M:\Drivers\Chrome\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.amazon.in/")
driver.maximize_window()
#driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()
#driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"email").send_keys("mohan444a3@gmail.com")
driver.find_element(By.XPATH,'//*[@id="continue"]').click()
driver.find_element(By.NAME,"password").send_keys("Mohan1999")
driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
time.sleep(3)

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Wireless mouse")
driver.find_element(By.ID,'nav-search-submit-button').click()

#to sort from low to high
#driver.find_element(By.XPATH,'//*[@id="a-autoid-0-announce"]').click() #to select the sort features
#driver.find_element(By.XPATH,'//*[@id="s-result-sort-select_1"]').click()  #to select the low to high

#to select particular mouse
mouse=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
mouse.click()

#take screenshot
#driver.save_screenshot("screen_shot#" + str(random.randint(0,101)) + ".png")

#To click on images
driver.find_element(By.XPATH,'//*[@id="landingImage"]').click()



#sliders means we can seee few pages scrolling left and right
#sliders=driver.find_elements(By.CLASS_NAME,'_cropped-image-link_style_fluidLandscapeImage__3eTVC _cropped-image-link_style_fluidImage__iJ3aE')
#print(len(sliders))

#links=driver.find_elements(By.TAG_NAME,'a')
#print(len(links))  #Total no of links in home page.
#driver.close()
#Ask kiran Whether the count of links will be changed for every execution or not
#bcz count is changing.
