# 求100~999之间的所有水仙花数
for x in range(100, 1000):
    a = x // 100
    b = x // 10 % 10
    c = x % 10
    if x == a ** 3 + b ** 3 + c ** 3:
        print(x)
    