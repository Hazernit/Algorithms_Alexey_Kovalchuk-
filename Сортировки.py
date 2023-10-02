def BubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = [4, 1, 6, 3, 2, 11, 7, 8]
print(BubbleSort(a))