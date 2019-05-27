import numpy as np


def merge_sort(a, left, right):
    if left < right:
        m = int((left + right)/2)
        print(a[left:m + 1])
        merge_sort(a, left, m)
        print(a[m+1:right+1])
        merge_sort(a, m + 1, right)
        merge(a, left, m, right)

def merge(a, left, m, right):
    n1 = int(m - left + 1)
    n2 = int(right - m)
    L = np.arange(0, n1+1)
    R = np.arange(0, n2+1)
    for i in range(0,n1):
        L[i] = a[left + i]
    for j in range(0, n2):
        R[j] = a[m + 1+j]
    i = 0
    j = 0
    L[n1]=1e9+9
    R[n2]=1e9+9
    for k in range(left, right + 1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1

def main():
    li = list(map(int,input().split()))
    array = np.array(li,dtype=int)
    r = len(li) - 1
    print(array)
    merge_sort(array, 0, r)
    print(array)


if __name__ == '__main__':
    main()

"""
48 38 65 97 76 13 27
"""
