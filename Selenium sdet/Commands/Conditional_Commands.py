from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime

from selenium.webdriver.common.by import By

serv_obj=Service('M:\Drivers\Chrome\chromedriver')
driver=webdriver.Chrome(service=serv_obj)
start=datetime.now()
driver.get('https://www.nopcommerce.com/en/register?returnUrl=%2Fen')
driver.maximize_window()
#is_displayed
#is_enabled
time.sleep(5)
downloads=driver.find_element(By.XPATH,'//*[@id="register-page"]/body/div[7]/header/nav/div[3]/div/ul[1]/li[2]/span')
print(downloads.is_displayed())
print(downloads.is_enabled())
print(downloads.is_selected())



end=datetime.now()
result=end-start
print("Total time:",result)





driver.close()