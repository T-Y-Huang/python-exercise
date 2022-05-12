1. 準備會使用到的套件與工具：


!pip install jieba # jieba 中文斷詞套件
!pip install wordcloud # wordcloud 文字雲視覺化套件
!pip install matplotlib # matplotlib 畫圖工具套件# txt檔案路徑


2. 將準備好的新聞語料來源進行斷詞


txt_file_path = "hw10.txt"

with open(txt_file_path, "r", encoding = "utf-8") as fn:
    lines = fn.readlines()
    lines = list(map(lambda x:x.strip(), lines))

import jieba

# 下載官方字典檔
!wget https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big

# 載入字典檔
jieba.load_userdict("檔案路徑")

tokens_1 = list(map(lambda x:list(jieba.cut(str(x), HMM = False)), lines))


3. 請將斷詞後的結果進行詞頻的計算存入 word_count 變數中，並且篩選出出現次數大於 5 次的字詞


from collections import defaultdict
word_count_d = defaultdict(int)
for sent in tokens_1: 
  for word in sent: 
    word_count_d[word] += 1

word_count_5 = {}
for word, count in word_count_d.items():
    if count > 5:
        word_count_5[word] = count

        
4. 利用 wordcloud 套件將剛剛整理好的資料製作成文字雲圖


import wordcloud
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt

# 下載中文字型檔
!wget https://github.com/odek53r/Data-Science-Camp/raw/main/SourceHanSerifK-Light.otf

wordcloud = WordCloud(
        background_color = 'white',
        font_path = '中文字型檔案的路徑', # 放入中文字型檔路徑
        colormap=matplotlib.cm.cubehelix,
        width = 1600,
        height = 800,
        margin = 2)

# wordcloud 套件 Input 需放入詞頻統計的 dict 型態變數
wordcloud = wordcloud.generate_from_frequencies(word_count_5)
plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
