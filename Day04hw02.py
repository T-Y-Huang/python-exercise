# 法一 enumerate
s = input("input:")

record = {} #記錄次數的dict容器
for char in s:# 踩每個字
    record[char] = [pos for pos, ind in enumerate(s, 1) if ind == char]
print(record)

# 法二 用位置來處理
s = input("input:")

dic = {}
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = [] 
    dic[s[i]].append(i+1)
print(dic)
