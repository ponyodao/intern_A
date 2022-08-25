from saitama_road import saitama_road
#from chiba_road import chiba_road
from send import send_mail
from get_list import get_item



chiba = get_item( "is:unread", 1)
chiba_address = chiba[0].split("<")
chiba_mail = chiba_address[1].replace(">","")
if chiba:
    print(chiba_mail,chiba[1])
    send_mail("intern.ohg.24a@gmail.com", chiba_mail, "地図情報を送信", "", "C:\\Users\\ryo2001\\OneDrive - 同志社大学\\デスクトップ\\エンカレッジ\\オープンハウス\\test\\RPA\\intern_A\\img\\chiba_water.pdf", cc=None)
else:
    send_mail("intern.ohg.24a@gmail.com", chiba_mail, "", "エラーです。", "", cc=None)
    
# allay_add = divide_address(address)

# if(allay_add[1] == "千葉市"):
#     chiba_road(chiba[0])
#   elif(allay_add[1] == "埼玉市"):
#     saitama_road(chiba[1])