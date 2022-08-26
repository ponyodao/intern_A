from audioop import add
import imp
from saitama_road import saitama_road
from saitama_water import saitama_water
from chiba_road import chiba_road
from send import send_mail
from get_list import get_item
from chiba_water import chiba_water
from divide_address import divide_address
import threading
import time

while True:

    mail = get_item( "is:unread", 1)

    try:
        divide = mail[0].split("<")
    except TypeError:
        print('新規メールなし')
    else:
        sender = divide[1].replace(">","")
        address = mail[1]

        if mail:
            if("千葉県" in address and "千葉市" in address):
                
                t1 = time.time()
                # chiba_water(address)
                # chiba_road(address)
                th1 = threading.Thread(target = chiba_water(address))
                th2 = threading.Thread(target = chiba_road(address))
               
                th1.start()
                th2.start()
                send_mail("intern.ohg.24a@gmail.com", sender, "千葉の下水道地図情報", "", ".\\img\\chiba_water.pdf", cc=None)
                send_mail("intern.ohg.24a@gmail.com", sender, "千葉の道路地図情報", "", ".\\img\\chiba_road.pdf", cc=None)
                t2 = time.time()

                elapsed_time = t2-t1
                print(f'経過時間：{elapsed_time}')
            elif("埼玉県" in address and "さいたま市" in address):
                
                t1=time.time()#計測開始
                # saitama_water(address)
                # saitama_road(address)
                th1 = threading.Thread(target = saitama_water(address))
                th2 = threading.Thread(target = saitama_road(address))
                th1.start()
                th2.start()
                
                send_mail("intern.ohg.24a@gmail.com", sender, "埼玉の下水道地図情報", "", ".\\img\\chiba_water.pdf", cc=None)
                send_mail("intern.ohg.24a@gmail.com", sender, "埼玉の道路地図情報", "", ".\\img\\chiba_water.pdf", cc=None)
                
                t2=time.time()#計測終了

                elapsed_time = t2-t1
                print(f'経過時間：{elapsed_time}')
            else:
                send_mail("intern.ohg.24a@gmail.com", sender, "", "県名から正確な住所を入力してください。", "", cc=None)
        

