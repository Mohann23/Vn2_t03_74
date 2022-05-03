from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME, "q").send_keys("selenium")   # one webelement / None
time.sleep(5)
auto_sugg = driver.find_elements(By.XPATH, "//li[@class='sbct']")  # list of webelements / emptylist
print(("length of autp_sugg: ", len(auto_sugg)))
#print("auto sugges: ", auto_sugg)
for i in auto_sugg:
    print(i.text)
    if i.text == "selenium ide":
        i.click()
        break  # without break getting stale element exception

time.sleep(10)
