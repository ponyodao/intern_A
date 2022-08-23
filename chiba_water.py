#千葉県下水
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from divide_address import divide_address
from selenium.webdriver.support.select import Select
import chromedriver_binary

import time

driver = webdriver.Chrome()
driver.get("http://s-page.tumsy.com/chibagesui/index.html");
time.sleep(3)
iframe = driver.find_element(By.XPATH,'/html/frameset/frame')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, '//*[@id="LinkButton1"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV1"]').click()


# if matches[1] == '中央区':
#     select.select_by_index(1)

# time.sleep(5)

# driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys("ginza six")
# driver.save_screenshot('screen.png')
# driver.save_screenshot('screen/screen2.png')
# time.sleep(5)
