import numpy as np


def modify(c):
    c[1, 1] = 1


a = np.zeros((4, 4))
b = a[1:3, 1:3]

print(a)
modify(b)
print(a)


