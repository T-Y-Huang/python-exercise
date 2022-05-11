num = input("請輸入數字(ex:1,2,3...):")
target = int(input("輸入總和:"))

nums_split = num.split(',')
nums = [int(j) for j in nums_split]

for n in nums:
    if target - n in nums:
        a = nums.index(n)
        b = nums.index(target - n)
print(min(a, b), max(a, b))
