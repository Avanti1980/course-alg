def gcd1(a, b):  # 暴力穷举
    for i in range(1, min(a, b) + 1):        # 最大公约数不会大于两者中的较小者
        if ((a % i == 0) and (b % i == 0)):  # 同时整除即为公约数
            gcd = i
    return gcd


def coef(a, b):  # 暴力穷举
    for i in range(b):        # 最大公约数不会大于两者中的较小者
        if (1-a*i) % b == 0:  # 同时整除即为公约数
            return i, int((1-a*i)/b)


def gcd2(a, b):  # 辗转相除
    a, b = max(a, b), min(a, b)
    while a % b:
        a, b = b, a % b
    return b


def gcd3(a, b):  # 更相减损
    while True:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
        else:
            return b


def gcd4(a, b):  # 改进的更相减损
    if a == b:
        return b
    while True:
        if not (a & 1) and not (b & 1):  # 均为偶 gcd(a,b) = 2 * gcd(a/2, b/2)
            return gcd4(a >> 1, b >> 1) << 1
        elif not (a & 1) and (b & 1):    # a偶 b奇 gcd(a,b) = gcd(a/2, b)
            return gcd4(a >> 1, b)
        elif (a & 1) and not (b & 1):    # a奇 b偶 gcd(a,b) = gcd(a, b/2)
            return gcd4(a, b >> 1)
        else:                            # 均为奇 更相减损 gcd(a,b) = gcd(a-b, b)
            a, b = max(a, b), min(a, b)
            return gcd4(a-b, b)


print(gcd1(2022, 1566))
print(coef(8, 9))
print(gcd2(2022, 1566))
print(gcd3(2022, 1566))
print(gcd4(2022, 1566))
