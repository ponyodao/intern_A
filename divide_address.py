import re
import jaconv
from replace_address import replace_address
def divide_address(address):

  # "丁目"があるかの判定　ないならx=0　
  # 　　　　　　　　　　　あるならx=1
  x = 0
  if "丁目" in address:
    x = 1

  # 三つの配列に分類　match[1],match[2],match[3]
  # match[2],match[3]をさらに分類
  address1 = replace_address(address)
  matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , address1)
  rematches1 = re.match(r'(..[市])(.+)',matches[2])
  town = re.split('[0-9]', matches[3])
  chome = matches[3].replace(town[0], "")
  if x == 0:
    return (matches[1],rematches1[1],rematches1[2],town[0],0,chome)
  else :
    splited_chome = chome.split("-")
    chome =  splited_chome[0]
    banchi = splited_chome[1]
    return (matches[1],rematches1[1],rematches1[2],town[0],chome,banchi)