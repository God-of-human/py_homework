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
    print(a[i+1], i+1)
    return i + 1

def main():
    li = list(map(int,input().split()))
    array = np.array(li,dtype=int)
    r = len(li) - 1
    p = 0
    QuickSort(array, p, r)
    print(array)

if __name__ == '__main__':
    main()
