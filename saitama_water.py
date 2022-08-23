import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
from get_geo import get_lat_lon_from_address

# import requests
# from bs4 import BeautifulSoup
# import time
# from tqdm import tqdm


print(get_lat_lon_from_address())

driver = webdriver.Chrome()
## フルパスを指定
URL = "https://www.sonicweb-asp.jp/saitama_g/map?theme=th_90#pos="+ get_lat_lon_from_address()
print(URL)
driver.get(URL)

iframe = driver.find_element(By.XPATH,'//*[@id="agreement_mask"]')
driver.switch_to.frame(iframe)

# #同意ボタン
driver.find_element(By.XPATH, '//*[@id="agree_btn_area"]/ul/li[1]/a').click()

time.sleep(7)

driver.save_screenshot('screen.png')

#driver.find_element(By.XPATH, '//*[@id="freeword_form"]/a').click()


# iframe = driver.find_element(By.XPATH,'//*[@id="agreement_mask"]')
# driver.switch_to.frame(iframe)

# #同意ボタン
# driver.find_element(By.XPATH, '//*[@id="agree_btn_area"]/ul/li[1]/a').click()
# time.sleep(3)

# adress_1="埼玉県さいたま市大宮区桜木町２丁目３３１"
# def get_lat_lon_from_address(address_l):
#     # """
#     # address_lにlistの形で住所を入れてあげると、latlonsという入れ子上のリストで緯度経度のリストを返す関数。
#     # >>>>get_lat_lon_from_address(['埼玉県さいたま市大宮区桜木町２丁目３３１'])
#     # [['35.712056', '139.762775'], ['35.707771', '139.768205']]
#     # """
#     url = 'http://www.geocoding.jp/api/'
#     latlons = []
#     for address in tqdm(address_l):
#         payload = {"v": 1.1, 'q': address}
#         r = requests.get(url, params=payload)
#         ret = BeautifulSoup(r.content,'lxml')
#         if ret.find('error'):
#             raise ValueError(f"Invalid address submitted. {address}")
#         else:
#             lat = ret.find('lat').string
#             lon = ret.find('lng').string
#             latlons.append([lat,lon])
#             time.sleep(10)
#     return latlons



#住所入力
#driver.find_element(By.XPATH, '//*[@id="freeword_text"]').send_keys("大宮")
#time.sleep(3)

#検索ボタン
#driver.find_element(By.XPATH, '//*[@id="freeword_form"]/a').click()

#施設名称クリック
#driver.find_element(By.XPATH, //*[@id="moku2"]/div[1]/table/tbody/tr[3]/td/a).click()

#driver.get("https://www.geocoding.jp/")

#time.sleep(10)
# driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(Keys.ENTER)
# driver.save_screenshot(r"C:\Users\ryo2001\OneDrive - 同志社大学\デスクトップ\エンカレッジ\オープンハウス\test\image\screen.png")
#time.sleep(20)
