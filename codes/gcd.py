def gcd(a, b):
    for i in range(1, min(a, b) + 1):        # 最大公约数不会大于两者中的较小者
        if ((a % i == 0) and (b % i == 0)):  # 同时整除即为公约数
            gcd = i
    return gcd


def coef(a, b):
    for x in range(1, b):         # 0 a 2a ... (b-1)a构成一个模b的剩余系
        if (1 - a * x) % b == 0:  # 若y也为整数
            y = int((1 - a * x) / b)
            return x, y


def Euclidean(a, b):  # 辗转相除
    while a % b:
        a, b = b, a % b
    return b


def Euclidean_coef(a, b):  # 辗转相除
    if a % b == 0:         # 递归停止条件：若b可以整除a
        return b, 1, 1 - int(a / b)
    else:
        d, x, y = Euclidean_coef(b, a % b)
        return d, y, x - int(a / b) * y


def gxjs(a, b):  # 更相减损
    while True:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
        else:
            return b


def gxjs_coef(a, b):  # 更相减损
    if a == b:        # 递归停止条件：a = b
        return b, 1, 0
    elif a > b:
        d, x, y = gxjs_coef(a - b, b)
        return d, x, y - x
    else:
        d, x, y = gxjs_coef(a, b - a)
        return d, x - y, y


def gxjs2(a, b):  # 改进的更相减损
    if a == b:
        return a
    while True:
        if not (a & 1) and not (b & 1):  # 均为偶 gcd(a,b) = 2 * gcd(a/2, b/2)
            return gxjs2(a >> 1, b >> 1) << 1
        elif not (a & 1) and (b & 1):    # a偶 b奇 gcd(a,b) = gcd(a/2, b)
            return gxjs2(a >> 1, b)
        elif (a & 1) and not (b & 1):    # a奇 b偶 gcd(a,b) = gcd(a, b/2)
            return gxjs2(a, b >> 1)
        else:                            # 均为奇 更相减损 gcd(a,b) = gcd(a-b, b)
            if a > b:
                return gxjs2(a - b, b)
            else:
                return gxjs2(a, b - a)


print(gcd(2023, 1024))
print(coef(2023, 1024))
print(Euclidean_coef(2024, 1024))
print(Euclidean_coef(2023, 1024))
print(Euclidean_coef(64, 1024))
print(gxjs_coef(2024, 1024))
print(gxjs_coef(2023, 1024))
print(gxjs_coef(64, 1024))
print(gxjs2(2024, 1024))
print(gxjs2(2023, 1024))
print(gxjs2(64, 1024))
