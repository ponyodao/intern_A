#千葉県　道路
import imp
import jaconv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from divide_address import divide_address
import chromedriver_binary
import time
from selenium.webdriver.support.select import Select
from PIL import Image

# address = "千葉県千葉市稲毛区穴川2丁目8番地"
# address = "千葉県千葉市稲毛区穴川町81"

def chiba_road(address):
    address_road = divide_address(address)
    driver = webdriver.Chrome()
    driver.get("https://webgis.alandis.jp/chiba12/portal/index.html")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="agree"]').click()
    time.sleep(3)
    # driver.find_element(By.XPATH, "/html/body/main/div[2]/div[1]/div[2]/p[2]/a/img").click()
    time.sleep(5)
    #若葉区
    driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/div/map/area[802]").click() 
    time.sleep(5)
    #検索マーククリック
    driver.find_element(By.XPATH, '//*[@id="sidemenu_tab_search"]').click()
    #住所検索をクリック
    driver.find_element(By.XPATH, '//*[@id="sidemenu_menu_search_drilldown_1"]').click()
    time.sleep(3)
    #稲毛区を選択
    s1 = Select(driver.find_element(By.XPATH, '//*[@id="srh_search_drilldown_1_attrvalue_1"]'))
    time.sleep(5)
    s1.select_by_value(address_road[2])
    time.sleep(5)
    #穴川町を検索
    s2 = Select(driver.find_element(By.XPATH, '//*[@id="srh_search_drilldown_1_attrvalue_2"]'))
    time.sleep(5)
    if address_road[4] == 0:
      s2.select_by_value(address_road[3])
    else:
      zenkaku_chome = jaconv.h2z(address_road[4], kana=False, ascii=False, digit=True)
      s2.select_by_value(address_road[3]+zenkaku_chome+"丁目")
    time.sleep(3)
    #81番地を検索
    s3 = Select(driver.find_element(By.XPATH, '//*[@id="srh_search_drilldown_1_attrvalue_3"]'))
    time.sleep(3)
    s3.select_by_value(address_road[5])
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="srh_search_drilldown_1_btn"]').click() ##最後の検索
    time.sleep(3)
    driver.save_screenshot(r"C:\\Users\\ryo2001\\OneDrive - 同志社大学\\デスクトップ\\エンカレッジ\\オープンハウス\\test\\RPA\\intern_A\\img\\chiba_road.png")
    #pdf変換
    image = Image.open(r"C:\Users\ryo2001\OneDrive - 同志社大学\デスクトップ\エンカレッジ\オープンハウス\test\RPA\intern_A\img\chiba_road.png")
    im_pdf = image.convert("RGB")
    im_pdf.save(r"C:\Users\ryo2001\OneDrive - 同志社大学\デスクトップ\エンカレッジ\オープンハウス\test\RPA\intern_A\img\chiba_road.pdf")