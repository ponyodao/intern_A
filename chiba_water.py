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
#区をクリック
driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV1"]').click()
#区を選択
s1 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV1"]'))
time.sleep(10)
s1.select_by_visible_text('稲毛区')
time.sleep(5)

#町をクリック
driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV2"]').click()
#町を選択
s2 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV2"]'))
time.sleep(10)
s2.select_by_visible_text('穴川町')
time.sleep(5)

#丁目をクリック
driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV3"]').click()
#丁目ありかなしを選択
s3 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV3"]'))
time.sleep(10)
s3.select_by_visible_text('丁目なし')
time.sleep(5)

#番地をクリック
driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV4"]').click()
#番地を選択
s4 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV4"]'))
time.sleep(10)
s4.select_by_visible_text('３１５番地')
time.sleep(5)

#検索
driver.find_element(By.XPATH, '//*[@id="btnAddSchDlgOK"]').click()
time.sleep(5)
#スクリーンショット
driver.save_screenshot(r"C:\Users\ryo2001\OneDrive - 同志社大学\デスクトップ\エンカレッジ\オープンハウス\test\RPA\intern_A\img\chiba_water.png")





# if matches[1] == '中央区':
#     select.select_by_index(1)

# time.sleep(5)

# driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys("ginza six")
# driver.save_screenshot('screen.png')
# driver.save_screenshot('screen/screen2.png')
# time.sleep(5)
