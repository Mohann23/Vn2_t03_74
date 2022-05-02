#we need to install request package through file-settings-projectINterpreter-request
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

start=datetime.now()

serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

#In this website we can find broken links
driver.get('http://www.deadlinkcity.com/')

#To find all the links
all_links=driver.find_elements(By.TAG_NAME,'a')
count=0  #to start the counting of links

for link in all_links:
    url=link.get_attribute('href') #getting all the href attributes
    try:
        res=requests.head(url) #storing all the href attribute urls into res
    except:
        None

    if res.status_code>=400: #taking all the error codes which are above 400 value
        print(url,' is broken link')
        count+=1  #of after the other will be added in loop
    else:
        print(url,"  is valid link")
print("Total number of broken links: ",count)
driver.close()
end=datetime.now()
result=end-start
print("Time taken:", result)