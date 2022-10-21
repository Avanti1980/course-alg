def gcd1(a, b):
    for i in range(1, min(a, b) + 1):        # 最大公约数不会大于两者中的较小者
        if ((a % i == 0) and (b % i == 0)):  # 同时整除即为公约数
            gcd = i
    return gcd


def gcd2(a, b):
    a, b = max(a, b), min(a, b)
    while a % b:
        a, b = b, a % b
    return b


def gcd3(a, b):
    while True:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
        else:
            return b


def gcd4(a, b):
    if a == b: return b
    while True:
        if not (a & 1) and not (b & 1):        # 均为偶
            return gcd4(a >> 1, b >> 1) << 1
        elif not (a & 1) and (b & 1):          # a偶 b奇
            return gcd4(a >> 1, b)
        elif (a & 1) and not (b & 1):          # a奇 b偶
            return gcd4(a, b >> 1)
        else:                                  # 均为奇
            a, b = max(a, b), min(a, b)
            return gcd4(a-b, b)


print(gcd1(10000, 65535))
print(gcd2(10000, 65535))
print(gcd3(10000, 65535))
print(gcd4(10000, 10240))
