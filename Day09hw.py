1. 將準備好的新聞語料資料庫（.txt）利用讀入到程式中


# txt檔案路徑
txt_file_path = "hw09.txt"

# 載入檔案到變數中
with open(txt_file_path, "r", encoding="utf-8") as fn:
    lines = fn.readlines()
    lines = list(map(lambda x: x.strip(),lines))
    
    
2. 使用 pip 安裝 `jieba` 斷詞套件與相關工具


# 安裝 jieba 中文斷詞套件
!pip install jieba

# 下載官方字典檔
!wget https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big

import jieba
jieba.load_userdict("jieba字典檔案路徑")


3. 試著用不同的斷詞模式將每篇新聞的原文進行斷詞


# 精確模式斷詞
tokens_1 = list(map(lambda x: list(jieba.cut(str(x), HMM=False)), lines))

# 全模式斷詞
tokens_2 = list(map(lambda x: list(jieba.cut(str(x), cut_all=True, HMM=False)), lines))

# 搜尋引擎模式斷詞
tokens_3 = list(map(lambda x: list(jieba.cut_for_search(str(x), HMM=False)), lines))


4. 將斷詞後的結果計算成每個字詞的出現次數（詞頻），並存成以「出現單字為 KEY、出現次數為 Value」的 dict 型態變數

Method 1 : 用 dictionary 儲存

# 法一
word_count = {}
for sent in tokens_1: # 放入斷詞之後的變數
  for word in sent:
    if word not in word_count:
      word_count[word] = 0
    word_count[word] += 1 
print(word_count)

# 法二
from collections import defaultdict
word_count = defaultdict(int)
for sent in tokens_1: 
  for word in sent: 
    word_count[word] += 1
    
 Method2: 用Counter記數（把斷詞全部放進列表中，再用 Counter 記數）

from collections import Counter
word_count_list = [item for sent in tokens_1 for item in sent]
Counter(word_count_list)
