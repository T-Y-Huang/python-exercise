➟ 口罩地圖 API 網址：https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json

1. 透過程式碼將檔案另存新檔下載到你的電腦中


import urllib.request as req # 載入網路連線模組
import json

# 收集
url = "https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json"

# 整理
with req.urlopen(url) as response: # python 做連線，給一個 response 物件
    data = json.load(response) # 用 response 讀取資料，把資料讀進變數 data

# 儲存
with open("mask.json", "w", encoding = "utf-8") as file:
    json.dump(data, file)
 
 
2. 計算各地區的藥局數量


items = data["features"] # 先把列表存在變數 items 中

from collections import defaultdict
med_count = defaultdict(int)

# 填入欄位名稱
for row in data['features']:
    conunty = row['properties']['county']
    if conunty == '':
      conunty = row['properties']['address'][0:3]
    med_count[conunty] += 1
print(med_count)


3. 計算每個地區的剩餘口罩數量(分成人的和小孩的)，並且從大到小排列


from collections import defaultdict

child_count = defaultdict(int)
adult_count = defaultdict(int) 
 
for row in data['features']:
    conunty = row['properties']['county']
    mask_child = row['properties']['mask_child']
    mask_adult = row['properties']['mask_adult']
    child_count[conunty] += mask_child
    adult_count[conunty] += mask_adult

# 排序
print(sorted(adult_count.items(), key=lambda x: x[1], reverse=True))
print(sorted(child_count.items(), key=lambda x: x[1], reverse=True))
