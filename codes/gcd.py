def gcd(a, b):
    for i in range(1, min(a, b) + 1):        # 最大公约数不会大于两者中的较小者
        if ((a % i == 0) and (b % i == 0)):  # 同时整除即为公约数
            gcd = i
    return gcd


def coef(a, b):
    for x in range(1, b):     # a 2a 3a ... ba构成一个模b的剩余系
        if (1-a*x) % b == 0:  # 若y也为整数
            y = int((1-a*x)/b)
            return x, y


def Euclidean(a, b):  # 辗转相除
    a, b = max(a, b), min(a, b)
    while a % b:
        a, b = b, a % b
    return b


def gxjs(a, b):  # 更相减损
    while True:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
        else:
            return b


def gxjs_mod(a, b):  # 改进的更相减损
    if a == b:
        return a, 1, 0
    while True:
        if not (a & 1) and not (b & 1):  # 均为偶 gcd(a,b) = 2 * gcd(a/2, b/2)
            d, x, y = gxjs_mod(a >> 1, b >> 1)
            return d << 1, x, y
        elif not (a & 1) and (b & 1):    # a偶 b奇 gcd(a,b) = gcd(a/2, b)
            d, x, y = gxjs_mod(a >> 1, b)
            return d, x << 1, y
        elif (a & 1) and not (b & 1):    # a奇 b偶 gcd(a,b) = gcd(a, b/2)
            d, x, y = gxjs_mod(a, b >> 1)
            return d, x, y << 1
        else:                            # 均为奇 更相减损 gcd(a,b) = gcd(a-b, b)
            if a > b:
                d, x, y = gxjs_mod(a-b, b)
                return d, x, y-x
            else:
                d, x, y = gxjs_mod(a, b-a)
                return d, x-y, y


print(gcd(2024, 1024))
print(coef(2023, 1024))
print(Euclidean(2024, 1024))
print(gxjs(2024, 1024))
print(gxjs_mod(8, 20))
