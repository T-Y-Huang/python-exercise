n = int(input("輸入:"))
def add1(n):
    return n+1

def isPrime(n):
    for i in range(2, n):
        if n == 1 or n == 2:
            return True
        elif n % i == 0:
            return False
    return True

def f(L:list, F): # 指定 L 為列表型態
    L1 = [F(l) for l in L]
    return L1

L = [2,3,4,5,6,7]
F = isPrime

print(f(L, F))
