import itertools

# ABC => ABC, ACB, BAC, BCA, CAB, CBA
s = input()
s = set(s) # 去除重複
s = sorted(s) # 排序
perm = list(itertools.permutations(s)) # 排列組合

result=[''.join(row) for row in perm]

print(result)
