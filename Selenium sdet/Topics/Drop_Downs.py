from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import datetime

from selenium.webdriver.support.select import Select

serv_obj=Service('M:\Drivers\Firefox\geckodriver')
driver=webdriver.Firefox(service=serv_obj)
driver.maximize_window()

#nopCommerce
driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')

#Country dropdown
drp_country_ele=driver.find_element(By.ID,"customerCurrency")
drp_country=Select(drp_country_ele)
#time.sleep(5)
#select option from dropdown
#drp_country.select_by_visible_text("Euro")
#drp_country.select_by_value("99")
#drp_country.select_by_index(100)  #for index we have to count manually so better go with other two




#capture all the elements and print them
all_options=drp_country.options #options is an in built function
print("Total number of options: ",len(all_options))

for opt in all_options:
    print(opt.text)

time.sleep(5)
#select option without using built in function
for opt in all_options:
    if opt.text=="Euro":
        opt.click()





time.sleep(4)
driver.quit()






