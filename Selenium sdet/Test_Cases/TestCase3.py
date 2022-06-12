from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("M:\Drivers\Chrome\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

'''
driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.NAME,'email').clear()
driver.find_element(By.NAME,'email').send_keys('mohan444a3@gmail.com')
driver.find_element(By.NAME,'pass').clear()
driver.find_element(By.NAME,'pass').send_keys('********************')
driver.find_element(By.NAME,'login').click()
time.sleep(5)

#click search key
search=driver.find_element(By.XPATH,'//i[@xpath="1"]')
search.click()

name=driver.find_element(By.XPATH,'//*[@id="facebook"]/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/label/input')
name.send_keys('Gajula Chakri')
name.submit()
'''



driver.get('https://money.rediff.com/gainers/nse')
driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/div[4]/a').click()
driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[7]/td[1]/a').click()
print(driver.title)
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[2]/ul/li[1]/a').click()
print(driver.title)
driver.close()



