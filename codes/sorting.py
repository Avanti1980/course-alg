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


def merge(a, l, m, r):

    # 子数组的长度
    n1, n2 = m - l + 1, r - m  

    # 创建临时数组
    L, R = [0] * (n1), [0] * (n2)  

    # 拷贝数据到临时数组L
    for i in range(0, n1):  
        L[i] = a[l + i]

    # 拷贝数据到临时数组R
    for j in range(0, n2):  
        R[j] = a[m + 1 + j]

    i, j, k = 0, 0, l

    # 归并L和R到a[l..r]
    while i < n1 and j < n2:  
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # 拷贝L的剩余元素
    while i < n1:  
        a[k] = L[i]
        i += 1
        k += 1

    # 拷贝R的剩余元素
    while j < n2:  
        a[k] = R[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l < r:
        m = int((l+r)/2)  # 取中间点分开
        merge_sort(a, l, m)
        merge_sort(a, m+1, r)
        merge(a, l, m, r)


def partition(a, l, r):

    # 最右元素作为主元
    pivot = a[r]

    # 小于主元的元素的存放位置 初始为最左
    i = l

    # l -> r-1 遍历其他元素
    for j in range(l, r):
        if a[j] <= pivot:
            # 小于主元的元素放到主元左边
            a[i], a[j] = a[j], a[i]
            i += 1  # 存放位置右移一位

    # 所有小于主元的元素已位于主元左边
    # 当前的i就是主元应该放的位置
    # 当前的a[i]大于主元
    a[i], a[r] = a[r], a[i]

    return i


def quick_sort(a, l, r):
    if l < r:
        m = partition(a, l, r)
        quick_sort(a, l, m-1)
        quick_sort(a, m+1, r)


a = [5, 2, 4, 6, 1, 3]
bubble_sort(a, len(a))
print(a)

a = [5, 2, 4, 6, 1, 3]
selection_sort(a, len(a))
print(a)

a = [5, 2, 4, 6, 1, 3]
insertion_sort(a, len(a))
print(a)

a = [5, 2, 4, 6, 1, 3]
merge_sort(a, 0, len(a)-1)
print(a)

a = [5, 2, 4, 6, 1, 3]
quick_sort(a, 0, len(a)-1)
print(a)
