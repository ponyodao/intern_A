import re
def divide_address(address):
  matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , address)
  print(matches[1])
  print(matches[2])
  print(matches[3])
if __name__ == '__main__':
  address = "東京都八王子市南大沢"
  divide_address(address)