from audioop import add
from saitama_road import saitama_road
from saitama_water import saitama_water
from chiba_road import chiba_road
from send import send_mail
from get_list import get_item
from chiba_water import chiba_water
from divide_address import divide_address



mail = get_item( "is:unread", 1)
divide = mail[0].split("<")
sender = divide[1].replace(">","")
address = mail[1]

if mail:
    if("千葉県" in address and "千葉市" in address):
        chiba_road(address)
        chiba_water(address)
        
        send_mail("intern.ohg.24a@gmail.com", sender, "地図情報を送信", "", "C:\\Users\\ryo2001\\OneDrive - 同志社大学\\デスクトップ\\エンカレッジ\\オープンハウス\\test\\RPA\\intern_A\\img\\chiba_water.pdf", cc=None)
        send_mail("intern.ohg.24a@gmail.com", sender, "地図情報を送信", "", "C:\\Users\\ryo2001\\OneDrive - 同志社大学\\デスクトップ\\エンカレッジ\\オープンハウス\\test\\RPA\\intern_A\\img\\chiba_road.pdf", cc=None)
    elif("埼玉県" in address and "さいたま市" in address):
        saitama_road(address)
        saitama_water(address)
        send_mail("intern.ohg.24a@gmail.com", sender, "地図情報を送信", "", "C:\\Users\\ryo2001\\OneDrive - 同志社大学\\デスクトップ\\エンカレッジ\\オープンハウス\\test\\RPA\\intern_A\\img\\saitama_water.pdf", cc=None)
        send_mail("intern.ohg.24a@gmail.com", sender, "地図情報を送信", "", "C:\\Users\\ryo2001\\OneDrive - 同志社大学\\デスクトップ\\エンカレッジ\\オープンハウス\\test\\RPA\\intern_A\\img\\saitama_road.pdf", cc=None)
    else:
        send_mail("intern.ohg.24a@gmail.com", sender, "", "千葉県、あるいは埼玉県の住所を入力してください。", "", cc=None)
    

