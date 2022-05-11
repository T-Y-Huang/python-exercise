# sol 1
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

d = {**dic1, **dic2, **dic3}
print(d)

# sol 2
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

dic1.update(dic2)
dic1.update(dic3)

d = dic1
print(d)
