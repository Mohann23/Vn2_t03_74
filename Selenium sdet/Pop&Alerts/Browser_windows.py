from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

serv_obj=Service('M:\Drivers\Chrome\chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.implicitly_wait(10)
'''
#single browser window
driver.get('https://www.vn2solutions.com:2096/cpsess2696531394/3rdparty/roundcube/?_task=mail&_mbox=INBOX')

window_id=driver.current_window_handle  #when we have single browser window
print(window_id)

driver.close()
'''

'''
#When we have countable browser windows
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

#click below link
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDs=driver.window_handles

parent_window=windowIDs[0]
child_window=windowIDs[1]

#to get title of the page
driver.switch_to.window(parent_window)
print("Title of the parent window",driver.title)

driver.switch_to.window(child_window)
print("title of the child window",driver.title)

driver.quit()
'''
'''
#When we have multiple browser windows
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

#click below link
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDs=driver.window_handles

for wind in windowIDs:
    driver.switch_to.window(wind)
    print(driver.title)

driver.quit()
'''

'''
#Closing specific browser windows
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

#click below link
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDs=driver.window_handles

for wind in windowIDs:
    driver.switch_to.window(wind)
    if driver.title=="OrangeHRM":
        #Now I am closing the parent window
        #We can use operator and close multiple windows at once
        driver.close()

'''





