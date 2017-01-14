from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re


import requests

browser = webdriver.Chrome("chromedriver.exe")
#browser.set_window_position(0,2000)               #將視窗放到下方藏起來，防止其他人按到而影響自動化流程

webheader = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
             'Referer' : 'https: // accounts.pixiv.net / login?lang = zh_tw & source = pc & view_type = page & ref = wwwtop_accounts_index'}
data = {'pixiv_id':'a5083a5083@gmail.com',
        'password': 'ab123456789ba',
        }

r = requests.Session()
r1 = r.get("https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",headers=webheader)
lt = re.findall(r'post_key[.\W\S\w\s]+?>',r1.text)
value = lt[0].split("value=")[1]
value = value[1:-2]
data['post_key'] = value
r2 = r.post("https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",data=data,headers=webheader)


cookies = r.cookies.get_dict()
print(cookies)

cookies_ = list(cookies.keys())
print(list(cookies.keys()))
browser.get("http://www.pixiv.net/")
browser.delete_all_cookies()             #先把瀏覽器的cookie全部刪除
#再依序添加新的cookie
for c in range(len(cookies_)):
    browser.add_cookie({'name': cookies_[c], 'value': cookies[cookies_[c]]})


browser.get("http://www.pixiv.net/recommended.php")
browser.find_element_by_id('enable-auto-view').click()#按下網頁的按鈕

#因為此網頁有使用javascript動態的變化功能，所以要執行javascript來模擬對網頁的動作
for i in range(5):  # 進行五次
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);') # 重複往下捲動
    time.sleep(1)  # 每次執行打瞌睡一秒

browser.back()     #瀏覽器到上一頁
browser.forward()  #瀏覽器到下一頁
browser.get("http://www.pixiv.net/member_illust.php?mode=medium&illust_id=60421168")
browser.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div[1]/div/div[6]/div').click()


