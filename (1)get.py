from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser

browser = webdriver.Chrome("chromedriver.exe")
browser.get('http://www.python.org')             #打開請求的URL，WebDriver 會等待頁面完全加載完成之後才會返回，即程序會等待頁面的所有內容加載完成，JavaScript 渲染完畢之後才繼續往下執行
                                                #注意：如果這裡用到了特別多的Ajax 的話，程序可能不知道是否已經完全加載完畢

# Ajax 是現今網站開發重要的環節，它利用舊有的技術（JavaScript、XML 等）實現了非同步請求 / 處理的機制，提供與使用者更多的互動，掀起 Web2.0 的波瀾。
# 傳統網頁在使用者提交資料後（亦即對伺服器發出請求），必須等到伺服器回應、重新整理頁面，才能繼續進行下一個動作，這段期間內使用者不能對該頁面做任何的存取。
# 而非同步請求允許使用者在發出請求到伺服器回應的期間內繼續使用頁面（例如：填寫剩餘表單），等到完成回應，瀏覽器僅更新部份資訊，藉以達到更有效的即時互動。

elem = browser.find_element_by_name('q')         #在網頁的html的原始檔中搜尋網頁name元素
elem = browser.find_element_by_xpath('//input[@name="q"]')
elem.send_keys("pycon")                         #在該元素上，輸入字串"pycon"
#elem.send_keys(Keys.RETURN)                                            #模擬點擊了Enter (\r+\n )，就像我們敲擊鍵盤一樣。我們可以利用Keys 這個類別來模擬鍵盤輸入
browser.find_element_by_name("submit").click()  #或是點擊網頁中的元素亦可
print(browser.page_source)                      #獲取網頁經過動態渲染後的網頁原始碼  (為 str 字串)
print(browser.get_cookies())
#這樣，我們就可以做到網頁的動態爬取了。

