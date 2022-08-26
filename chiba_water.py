#千葉県下水
import jaconv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from divide_address import divide_address
from selenium.webdriver.support.select import Select
import chromedriver_binary
from PIL import Image

import time

# address = "千葉県千葉市稲毛区穴川2丁目8番地"
# address = "千葉県千葉市稲毛区穴川町371"

def chiba_water(address):
    address_water = divide_address(address)
    driver = webdriver.Chrome()
    driver.get("http://s-page.tumsy.com/chibagesui/index.html");
    time.sleep(5)
    iframe = driver.find_element(By.XPATH,'/html/frameset/frame')
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH, '//*[@id="LinkButton1"]').click()
    time.sleep(7)
    #区をクリック
    driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV1"]').click()
    #区を選択
    s1 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV1"]'))
    time.sleep(3)
    s1.select_by_visible_text(address_water[2])
    time.sleep(3)
    #町をクリック
    driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV2"]').click()
    #町を選択
    s2 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV2"]'))
    time.sleep(3)
    s2.select_by_visible_text(address_water[3])
    time.sleep(3)
    #丁目をクリック
    driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV3"]').click()
    s3 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV3"]'))
    time.sleep(3)
    #丁目ありかなしを選択
    if len(address_water) == 5:
        s3.select_by_visible_text('丁目なし')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV4"]').click()
        s4 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV4"]'))
        all_options = s4.options
        time.sleep(3)
        zenkaku_banchi = jaconv.h2z(address_water[4], kana=False, ascii=False, digit=True)
        if "番地" in all_options[1].text:
         s4.select_by_visible_text(zenkaku_banchi+"番地")
        else:
         s4.select_by_visible_text(zenkaku_banchi+"番")
    else:
        zenkaku_chome = jaconv.h2z(address_water[4], kana=False, ascii=False, digit=True)
        s3.select_by_visible_text(zenkaku_chome+'丁目')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV4"]').click()
        s4 = Select(driver.find_element(By.XPATH, '//*[@id="ELM_CMB_LEV4"]'))
        all_options = s4.options
        time.sleep(3)
        zenkaku_banchi = jaconv.h2z(address_water[5], kana=False, ascii=False, digit=True)
        if "番地" in all_options[1].text:
          s4.select_by_visible_text(zenkaku_banchi+"番地")
        else:
          s4.select_by_visible_text(zenkaku_banchi+"番")
    time.sleep(3)
    #検索
    driver.find_element(By.XPATH, '//*[@id="btnAddSchDlgOK"]').click()
    time.sleep(3)

    #スクリーンショット
    driver.save_screenshot(".\\img\\chiba_water.png")
    #pdf変換
    image = Image.open(".\\img\\chiba_water.png")
    im_pdf = image.convert("RGB")
    im_pdf.save(".\\img\\chiba_water.pdf")