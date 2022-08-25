import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from get_geo import get_lat_lon_from_address
from PIL import Image

# import requests
# from bs4 import BeautifulSoup
# import time
# from tqdm import tqdm

def saitama_water(address):
    driver = webdriver.Chrome()
    ## フルパスを指定
    URL = "https://www.sonicweb-asp.jp/saitama_g/map?theme=th_90#pos="+ get_lat_lon_from_address(address)
    print(URL)
    driver.get(URL)

    iframe = driver.find_element(By.XPATH,'//*[@id="agreement_mask"]')
    driver.switch_to.frame(iframe)

    # #同意ボタン
    driver.find_element(By.XPATH, '//*[@id="agree_btn_area"]/ul/li[1]/a').click()

    time.sleep(7)

    driver.save_screenshot(r"C:\\Users\\ryo2001\\OneDrive - 同志社大学\\デスクトップ\\エンカレッジ\\オープンハウス\\test\\RPA\\intern_A\\img\\saitama_road.png")
       #pdf変換
    image = Image.open(r"C:\Users\ryo2001\OneDrive - 同志社大学\デスクトップ\エンカレッジ\オープンハウス\test\RPA\intern_A\img\saitama_water.png")
    im_pdf = image.convert("RGB")
    im_pdf.save(r"C:\Users\ryo2001\OneDrive - 同志社大学\デスクトップ\エンカレッジ\オープンハウス\test\RPA\intern_A\img\saitama_water.pdf")

