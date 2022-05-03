# waits in selenium
# implicit wait, explicit wait, fluent wait
# driver.implicitly_wait(10) - will be applicable through out the driver session
# this wait is applicable only for webelement

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
#driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("asjhghdgf@gmail.com") #username
driver.implicitly_wait(2)
driver.find_element(By.ID, "password").send_keys("asdkjdhfdshghf") #password
driver.implicitly_wait(0)
#e3
#e4
#e5
#....
#driver.implicitly_wait(15)
# x =10
# x = 20
#print(x)
