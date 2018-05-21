
for x in range(100,1000):
    gewei = x % 10
    shiwei = (x % 100)//10
    baiwei = x // 100
    if x == gewei**3 + shiwei**3+ baiwei**3:
        print(x)