def bubble_sort(a, n):
    t = 0
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]


def selection_sort(a, n):
    for i in range(n):
        min_index = i
        min_val = a[i]
        for j in range(i+1, n):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


a = [5, 2, 4, 6, 1, 3]

if len(a) > 1:

    b = a
    bubble_sort(b, len(b))
    print(b)

    b = a
    selection_sort(b, len(b))
    print(b)
