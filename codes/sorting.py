def bubble_sort(a, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
        print(i+1, a)


def selection_sort(a, n):
    for i in range(len(a)):
        min_index = i
        min_val = a[i]
        for j in range(i, len(a)):
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
