n = 30
state = [0 for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if j % i == 0:
            state[j] = 1 - state[j]
print(state)