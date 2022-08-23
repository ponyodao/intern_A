#埼玉県道路
from email.headerregistry import Address
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from divide_address import divide_address
from get_geo import get_lat_lon_from_address
from selenium.webdriver.support.select import Select
import chromedriver_binary
import time
address = "埼玉県越谷市レイクタウン3丁目1番地1"
URL = "https://www.sonicweb-asp.jp/saitama_g/map?theme=th_31#pos=" + get_lat_lon_from_address()
driver = webdriver.Chrome()
driver.get(URL);
time.sleep(3)
iframe = driver.find_element(By.XPATH,'//*[@id="agreement_mask"]')
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, '//*[@id="agree_btn_area"]/ul/li[1]/a').click()
time.sleep(5)
driver.save_screenshot('screen.png')
