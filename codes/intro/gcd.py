def gcd(a: int, b: int) -> int:
    d = 1
    for i in range(2, min(a, b) + 1):  # 最大公约数不会大于两者中的较小者
        if a % i == 0 and b % i == 0:  # 同时整除即为公约数
            d = i
    return d


def coef(a: int, b: int, t: int, d: int) -> tuple[int, int]:
    if t % d != 0:
        raise ValueError("t必须是最大公约数d的倍数")
    a, b, t = a // d, b // d, t // d  # 此时 a b 互素
    for x in range(1, b):         # 0 a 2a ... (b-1)a 构成一个模 b 的剩余系
        if (a * x) % b == 1:
            y = (1 - a * x) // b
            return t * x, t * y


def Euclidean(a: int, b: int) -> int:  # 辗转相除
    while b:
        a, b = b, a % b
    return a


# 返回 (d, x, y) 使得 ax + by = d = gcd(a, b)
def Euclidean_extended(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = Euclidean_extended(b, a % b)
        return d, y, x - (a // b) * y


def Euclidean_coef(a: int, b: int, t: int) -> tuple[int, int]:
    d, x, y = Euclidean_extended(a, b)
    if t % d != 0:
        raise ValueError("t必须是最大公约数d的倍数")
    t = t // d
    return t * x, t * y


def alternative_subtraction(a: int, b: int) -> int:  # 更相减损
    shift = 0  # 最大公约数的质因子分解中 2 的幂次
    while not (a & 1) and not (b & 1):  # a、b 均为偶 2是公因子
        a >>= 1  # a <- a / 2
        b >>= 1  # b <- b / 2
        shift += 1
    while True:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
        else:
            return b << shift


def gcd_opt(a: int, b: int) -> int:  # 改进的更相减损
    shift = 0  # 最大公约数的质因子分解中 2 的幂次
    while not (a & 1) and not (b & 1):  # 均为偶 2是公因子
        a >>= 1  # a <- a / 2
        b >>= 1  # b <- b / 2
        shift += 1
    # 此时 2 已不再是公因子
    while not (a & 1):  # a 不断除以 2 变成奇数
        a >>= 1
    while b:
        while not (b & 1):  # b 不断除以 2 变成奇数
            b >>= 1
        if a < b:
            a, b = b, a  # 确保 a 大 b 小
        a -= b  # 更相减损 新的 a 必为偶
    return a << shift


a, b, t = 98, 63, 21

d = gcd(a, b)
print(d)
x, y = coef(a, b, t, d)
print(x, y)

d = Euclidean(a, b)
print(d)

x, y = Euclidean_coef(a, b, t)
print(x, y)

d = alternative_subtraction(a, b)
print(d)

d = gcd_opt(a, b)
print(d)
