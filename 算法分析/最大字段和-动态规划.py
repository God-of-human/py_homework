"""
如果b[j] 是节点j之前的最大子段和，那么，
整个序列的最大子段和即为b[j] 中的最大值
"""
import numpy as np

def maxSum(n, a, base):
    sum = 0
    b = 0
    leftIndex = 0
    for i in range(n):
        if b > 0:
            b += a[i]
        else:
            b = a[i]
            leftIndex = i + 1
        if b > sum:
            base[0] = leftIndex
            sum = b
            base[1] = i + 1
    return sum

def main():
    a = np.array(input().split(), dtype=np.int)
    n = a.size
    base = [0, 0]
    print(maxSum(n, a, base))
    print(base[0])
    print(base[1])

if __name__ == '__main__':
    main()

"""
样例输入
-2 11 -4 13 -5 -2
"""