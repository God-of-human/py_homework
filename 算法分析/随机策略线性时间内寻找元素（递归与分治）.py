"""
RANDOMIZED-SELECT(A, p, r, i)
	if p==r
	    return A[p]
	q = RANDOMIZED-PARTITION(A, p, r)
	k = q-p+1
	if i == k
	    return A[q]
	elseif  i <k
	    return RANDOMIZED-SELECT(A, p, q-1, i)
	else return RANDOMIZED-SELECT(A, q+1, r, i-k)
时间复杂度：O(n）
"""
import numpy as np
"""
以A[r]为基准，将数组A[p..r] 划分成3段，
并满足A[p..q-1] ≤ A[q] ≤ A[q+1..r]
划分结束后，原A[r]就放在划分后q的位置

"""
def Partition(a, p, r):
    #此时r 恰好时数组的最后一个下标
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            #当第一个元素即小于a[r],就没有交换
            a[i], a[j] = a[j], a[i]
    #最后一次交换即将a[r]放到了划分时的位置，在此处划分
    a[i+1], a[r] = a[r], a[i+1]
    #返回坐标
    return i + 1

#随机选出一个元素划分
def RandomizedPartition(a, p, r):
    #随机
    i = np.random.randint(p, r)
    a[i], a[p] = a[p], a[i]
    return Partition(a, p, r)

"""
递归求解：
计算子数组A[p..q]中元素个数k。
如果i=k，则第i小的元素为A[q]；
如果i<k，则第i小的元素在子数组A[p..q-1]中；
如果i>k，则第i小的元素在子数组A[q+1..r]中，
且是该数组第i-k小元素。
"""
def RandomizedSelsct(a, p, r, i):
    if p == r:
        return a[p]
    #q 表示划分的的位置
    q = RandomizedPartition(a, p, r)
    #k 子数组元素个数
    k = q - p +1
    #i 表示第i小
    if i == k:
        return a[q]
    elif i < k:
        return RandomizedSelsct(a, p, q - 1, i)
    else:
        return RandomizedSelsct(a, q + 1, r, i - k)

def main():
    #输入一组数
    array = np.array(input().split(),dtype = np.int)
    i = int(input())
    r = len(array) - 1
    p = 0
    print(RandomizedSelsct(array, p, r,i))

if __name__ == '__main__':
    main()
