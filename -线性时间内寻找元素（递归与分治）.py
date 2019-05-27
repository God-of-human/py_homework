import numpy as np

def QuickSort (a, p, r):
    if p < r:
        q = Partition(a, p, r)
        QuickSort(a, p, q-1)
        QuickSort(a, q+1, r)

def Partition(a, p, r):
    x = a[r]
    i = p - 1
    count = p

    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

def Select(a, p, r, i):
    n = r - p + 1
    if(n < 50):
        QuickSort(a, p, r)
        return a[p + i - 1]
    else:
        for j in range( 0, (n - 5) // 5 + 1):
            QuickSort(a, p + 5 * j, p + 5 * j + 4)
            a[p + 5 * j + 2],a[p + j] = a[p + j], a[p + 5 * j + 2]
        x = Select(a, p , p + (r - p -4)//5, (r -p - 4)//10)
        a[r], x = x, a[r]
        q = Partition(a, p, r)
        k = q - p + 1
        if i == k:
            return a[q]
        elif i < k:
            return Select(a, p, q - 1, i)
        else:
            return Select(a, q + 1, r, i - k)


def main():
    li = list(map(int,input().split()))
    i = int(input())
    array = np.array(li,dtype=int)
    r = len(li) - 1
    p = 0
    print(Select(array, p, r, i))

if __name__ == '__main__':
    main()
