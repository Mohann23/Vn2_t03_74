from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
from datetime import datetime

#Chrome link
serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

#Testautomation practice page
driver.get('http://itera-qa.azurewebsites.net/home/automation')

'''
#1 select specific checkbox
driver.find_element(By.ID,'tuesday').click()
'''

#2 Select all the checkbox (we need to use find_elements
check_boxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains( @id,'day')]")
#To write the xpath of this I have checked the video sdet session 7 time 10 mins

#print(len(check_boxes)) #7


'''
#Approach 1

for i in range(len(check_boxes)):
    check_boxes[i].click()
'''

'''
#Approach 2

for checkbox in check_boxes:
    checkbox.click()
'''
'''
#3.select multiple checkboxes by choice

for checkbox in check_boxes:
    weekname=checkbox.get_attribute('id')
    if weekname=='monday' or weekname=='sunday':  #when you need both monday and sunday
        checkbox.click()
        
'''
'''
#4.select last 2 check boxes
#range(5,7)--> saturday(6),sunday(7)
#total number of elements-2=starting index
for i in range(len(check_boxes)-2,len(check_boxes)):
    check_boxes[i].click()
#This helps us to select the elements in one sequence
'''
'''
#5. select first 2 checkboxes
for i in range(len(check_boxes)):
    if i<2:
        check_boxes[i].click()
'''
time.sleep(5)
#6. clear all the check boxes
#When you use this you also need to do the first approach if the checkboxes are not selected
'''
for checkbox in check_boxes:
    if checkbox.is_selected():
        checkbox.click()
'''
'''
#or
for i in check_boxes:
    i.click()
time.sleep(5)
'''
driver.quit()





