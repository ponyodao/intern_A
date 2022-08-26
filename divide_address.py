import re
import jaconv
from replace_address import replace_address
def divide_address(address):
  address1 = replace_address(address)
  matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , address1)
  matches = re.match(r'(...??[都道府県])(.+)', address1)
  matches1 = re.match(r'(.+?[市])(.+)', matches[2])
  matches2 = re.match(r'(.+?[区])(.+)', matches1[2])
  town = re.split('[0-9]', matches2[2])
  chome1 = matches2[2].replace(town[0], "")
  if "-" in chome1:
    splited_chome = chome1.split("-")
    chome =  splited_chome[0]
    banchi = splited_chome[1]
    return (matches[1],matches1[1],matches2[1],town[0],chome,banchi)
  else:
    return (matches[1],matches1[1],matches2[1],town[0],chome1)
















import re
import jaconv
from replace_address import replace_address
def divide_address(address):
  address1 = replace_address(address)
  matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , address1)
  matches = re.match(r'(...??[都道府県])(.+)', address1)
  matches1 = re.match(r'(.+?[市])(.+)', matches[2])
  matches2 = re.match(r'(.+?[区])(.+)', matches1[2])
  town = re.split('[0-9]', matches2[2])
  chome1 = matches2[2].replace(town[0], "")
  if "-" in chome1:
    splited_chome = chome1.split("-")
    chome =  splited_chome[0]
    banchi = splited_chome[1]
    return (matches[1],matches1[1],matches2[1],town[0],chome,banchi)
  else:
    return (matches[1],matches1[1],matches2[1],town[0],chome1)








