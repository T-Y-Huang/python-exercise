➟ PTT web 網址：https://www.ptt.cc/bbs/Gossiping/index.html

1. 將ptt1八卦版每篇文章網址抓出來
2. 透過文章網址將內文一起抓出來

# 把解析 html 網頁整理成函式使用
def getRoot(url):
    import urllib.request as req
    
    request = req.Request(url, headers = {
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    return root
   
# 給八卦版網址
url_gossiping = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 找全部的標題標籤
items = getRoot(url_gossiping).find_all("div", class_='title')

result = []
for item in items:
    if item.a != None:
        title = item.a.string
        url = "https://www.ptt.cc" + item.a["href"]
        content = getRoot(url).find("div", class_="bbs-screen bbs-content").text
        result.append([title, url, content])

import pandas as pd
pd.DataFrame(result, columns=['title', 'url','content']).to_excel('content1.xlsx')


3. 試著用程式碼抓取下一頁的內容（透過抓取按鈕「上頁」的網址，來獲得下一頁的 HTML），並且觀察看看每頁的網址的改變


pageURL = url_gossiping
count = 0
while count<3:
    nextPage = getRoot(pageURL).find("a", string="‹ 上頁")
    pageURL = "https://www.ptt.cc" + nextPage["href"]
    print(pageURL)
    count+=1
