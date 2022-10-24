def bubble_sort(a, n):
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]


def selection_sort(a, n):
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]


def insertion_sort(a, n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


a = [5, 2, 4, 6, 1, 3]

b = [5, 2, 4, 6, 1, 3]
bubble_sort(b, len(b))
print(b)

b = [5, 2, 4, 6, 1, 3]
selection_sort(b, len(b))
print(b)

b = [5, 2, 4, 6, 1, 3]
insertion_sort(b, len(b))
print(b)
