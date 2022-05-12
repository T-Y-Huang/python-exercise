# 法一 費式數列
'''
count = 0，a = 1，b = 1
count = 1，a = 1，b = 2
count = 2，a = 2，b = 3
count = 3，a = 3，b = 5
count = 4，a = 5，b = 8
'''
n = int(input("輸入:"))

climb = 1 # 從第一階開始
a, b = 0, 1
while climb < n+1: # 走到幾階
    a, b = b, a+b
    climb += 1
print(b)

# 法二
def climbStairs(n: int) -> int:
    W = [0, 1, 2] # 記錄前三階的走法
    for i in range(3, n+1):
        W.append(W[i - 2] + W[i - 1]) # 把下一階的總走法記錄到 W 中
    return W[n]
print(climbStairs(5))
