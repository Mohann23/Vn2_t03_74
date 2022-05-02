'''New Assignment!!!!
Open the test automation practice window
1.select the alert window
2.in wikipedia we need to search for selenium
3.open all the links displayed after that
4.capture the titles of all the pages
5.close all windows at once'''


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

serv_obj=Service('M:\Drivers\Chrome\chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

#open Test automation practice webpage
driver.get("https://testautomationpractice.blogspot.com/")

#Alert
driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button').click()
alert_window=driver.switch_to.alert
#print(alert_window.text)
alert_window.accept()   #To click okay on the alert window

#sending the values into the search button
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Selenium")
driver.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input').click()

#Used to name all the tab's and toggle between them
windowsIDs=driver.window_handles

#results_1
link1=driver.find_element(By.LINK_TEXT,"Selenium")
link1.click()
print(link1.text)


#to go to the first page so that we can click next link
parent_window=windowsIDs[0]
driver.switch_to.window(parent_window)

#result_2
link2=driver.find_element(By.LINK_TEXT,"Selenium in biology")
link2.click()
print(link2.text)
driver.switch_to.window(parent_window)

link3=driver.find_element(By.LINK_TEXT,"Selenium (software)")
link3.click()
print(link3.text)
driver.switch_to.window(parent_window)

link4=driver.find_element(By.LINK_TEXT,"Selenium disulfide")
link4.click()
print(link4.text)
driver.switch_to.window(parent_window)

link5=driver.find_element(By.LINK_TEXT,"Selenium dioxide")
link5.click()
print(link5.text)
driver.switch_to.window(parent_window)

'''driver.switch_to.window(link1)
print(driver.title)
driver.quit()


for wind in windowsIDs:
    print(driver.current_window_handle.title())
'''
driver.quit()







