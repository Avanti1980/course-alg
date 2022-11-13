import random

# random.seed(0)


d = [1 for i in range(n)]
p = [-1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if X[j] < X[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            p[i] = j

# print('d: %s' % d)
# print('p: %s' % p)

lis_len_index = d.index(max(d))
lis = [X[lis_len_index]]
pos = p[lis_len_index]
while pos != -1:
    lis.append(X[pos])
    pos = p[pos]
lis.reverse()

n = 8
X = [i for i in range(n)]
random.shuffle(X)
print('X =', X)
print('LIS =', lis)
