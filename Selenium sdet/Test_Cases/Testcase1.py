#Test case

#1.Open web browser (chrome/fire/ie)
#2.Open URL http://opensource-demo.orangehrmlive.com/
#3.Provide username (admin)
#4.Provide password (admin123)
#5.click on login.
#6.Capture title of the dashboard page (Actual Title)
#7.Verify title of the page: "Dashboard/ nopcommerce administration" (expected)
#8.Close browser.


#selenium 3

'''from selenium import webdriver

driver=webdriver.Chrome(executable_path="M:\Drivers\Chrome\chromedriver")
driver.get("http://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Login Test passed!!")
else:
    print("Login test failed!!")

driver.close()

'''

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("M:\Drivers\Chrome\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.get("http://opensource-demo.orangehrmlive.com/")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Login Test Passed!!!")
else :
    print("Login failed!!")

driver.close()
'''
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("M:\Drivers\Chrome\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.NAME,"Email").clear()  #used to clear when the gaps are filled for examples
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
#i have used xpath bcz i was facing some issues.
act_name=driver.title
exp_name="Dashboard / nopCommerce administration"
if act_name==exp_name:
    print("Test successfullllll")
else:
    print("Test failed!!")

driver.close()

'''
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("M:\Drivers\Chrome\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.com/")
driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()
driver.find_element(By.NAME,"email").send_keys("mohan444a3@gmail.com")
driver.find_element(By.ID,"continue").click()
driver.find_element(By.ID,"ap_password").send_keys("Mohan1999")
driver.find_element(By.ID,"signInSubmit").click()

time.sleep(5)
driver.close()
'''





























