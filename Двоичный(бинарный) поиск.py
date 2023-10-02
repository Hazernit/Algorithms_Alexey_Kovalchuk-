# O(nlogn)
def lbs(a, x):
    l = -1
    r = len(a) - 1
    while l + 1 != r:
        c = (l + r) // 2
        if a[c] < x:
            l = c
        else:
            r = c
    return r

def rbs(a, x):
    l = 0
    r = len(a)
    while l + 1 != r:
        c = (l + r) // 2
        if a[c] > x:
            r = c
        else:
            l = c
    return l

a = [1, 3, 20, 20, 20, 20, 21, 27, 30]
x = 20
print(lbs(a, x))
print(rbs(a, x))

a = [1, 3, 20, 20, 20, 20, 23, 23, 23, 27, 30]
x = 21
# Выводит ПЕРВЫЙ индекс ближайшего следующего за нашем
print(lbs(a, x))
# Выводит ПОСЛЕДНИЙ индекс ближайшего предыдущего к нашему числу
print(rbs(a, x))
