import numpy as np

def RandomizedQuickSort (a, p, r):
    if p < r:
        q = RandomizedPartition(a, p, r)
        RandomizedQuickSort(a, p, q-1)
        RandomizedQuickSort(a, q+1, r)

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

def RandomizedPartition(a, p, r):
    i = np.random.randint(p, r)
    a[i], a[p] = a[p], a[i]
    return Partition(a, p, r)

def RandomizedSelsct(a, p, r, i):
    if p == r:
        return a[p]
    q = RandomizedPartition(a, p, r)
    k = q - p +1
    if i == k:
        return a[q]
    elif i < k:
        return RandomizedSelsct(a, p, q - 1, i)
    else:
        return RandomizedSelsct(a, q + 1, r, i - k)


def main():
    li = list(map(int,input().split()))
    i = int(input())
    array = np.array(li,dtype=int)
    r = len(li) - 1
    p = 0
    print(RandomizedSelsct(array, p, r,i))

if __name__ == '__main__':
    main()
