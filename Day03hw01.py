a = int(input("輸入:"))
b = int(input("輸入:"))

# 定義自除數
def sdn(n):
    n_str = str(n)
    n_list = [i for i in n_str]
    for j in n_list:
        if int(j) == 0:
            return False
        elif n % int(j) != 0:
            return False
    return True

# 範圍內的自除數列表
sdn_list = [num for num in range(a, b+1) if sdn(num)]

# 法一
diff_max = 0 # 先定義最大差距是0
for order in range(1, len(sdn_list)):
    diff = sdn_list[order] - sdn_list[order-1] # 倆倆數字的差距
    if diff > diff_max: # 如果新的一個數字大於一開始的定義:0
        diff_max = diff # 用新的數字取代0(目前最大的差距)
        diff_index = order # 紀錄出現最大差距的數字位置
print(sdn_list[diff_index-1], sdn_list[diff_index])

# 法二
# 倆倆差距值的列表
diff_list = []
for order in range(1, len(sdn_list)):
    diff = sdn_list[order] - sdn_list[order-1]
    diff_list.append(diff)

# 找出差距值最大在列表的哪個位置
for m in diff_list:
    if m == max(diff_list):
        ans = diff_list.index(m)

print(sdn_list[ans], sdn_list[ans+1])
