import numpy as np

def maxSubSum(a, left, right, base):
    sum = 0
    if left == right:
        sum = a[left] if a[left] > 0 else 0
    else:
        center = (left + right) // 2
        leftsum = maxSubSum(a, left, center,base)
        rightsum = maxSubSum(a, center + 1, right,base)
        lefts = 0
        s1 = 0
        for i in range(center, left -1,-1):
            lefts += a[i]
            if lefts > s1:
                s1 = lefts
                base[0] = i + 1
        s2 = 0  
        rights = 0
        for j in range(center + 1 , right + 1):
            rights += a[j]
            if rights > s2:
                s2 = rights
                base[1]= j + 1
        sum = s1 + s2
        if sum < leftsum:
            sum = leftsum
        if sum < rightsum:
            sum = rightsum
    return sum


def main():
    a = np.array(input().split(), dtype=np.int)
    n = a.size
    #列表存储坐标
    base = [0,0]
    print(maxSubSum(a, 0, n - 1, base))
    print(base[0])
    print(base[1])

if __name__ == '__main__':
    main()
