"""
矩阵连乘，其递归式自向上在计算过程中保存子问题的答案，
每个子问题只解决一次，后面计算时，只要简单查看一下得到其结果
m[i][j]存放A[i:j]所需最少数乘次数
p表示第一个矩阵的行数和第一个矩阵到第n个矩阵的列数
"""
import numpy as np
def Matrix_chain(p, n):
    m = np.zeros((n+1, n+1),dtype = np.int)
    s = np.zeros((n+1, n+1),dtype = np.int)
    for i in range(1, n ):
        m[i, i] = 0
    #思考计算顺序，从上到下，从左到右，
    #考虑i和j之间的关系，以及i和len之间的关系
    for len in range(2, n + 1):
        for i in range(1, n - len + 2):
            j = i + len- 1
            m[i, j] = 1000000
            for k in range (i, j):
                q = m[i, k] + m[k + 1, j] + p[i-1] * p[k] * p[j]
                if q < m[i, j]:
                    m[i, j] = q
                    s[i, j] = k
    print(m[1:, 1:])
    print(s[1:, 1:])
    print(Print_optim(s, 1, n))

def Print_optim(s, i, j):
    if i == j:
        s1 = "A" + str(i)
    else :
        s1 = "(" +Print_optim(s, i, s[i, j])+ Print_optim(s, s[i, j] + 1, j) + ")"
    return s1




def main():
    n = int(input())
    li = list(map(int, input().split()))
    p = np.array(li, dtype = int)
    Matrix_chain(p, n)

if __name__ == '__main__':
    main()


"""
 6
 30 35 15 5 10 20 25
"""