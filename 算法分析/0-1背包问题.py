"""
m[i][j]即背包容量为j，可选择物品为i，i+ 1，n是 时，0 -1 背包问题的最优值
"""
import numpy as np
def knapsack(v, w, c, n):
    #创建矩阵
    m = np.zeros((n + 1, c + 1),dtype=np.int)
    for j in range(w[n - 1], c + 1):
        m[n, j] = v[n - 1]
    for i in range (n - 1, 1, -1):
        jmax = min(w[i - 1] - 1, c)
        for j in range(0, jmax + 1):
            m[i, j] = m[i + 1, j]
        for j in range(w[i - 1], c + 1):
            m[i, j] = max(m[i + 1, j], m[i + 1, j - w[i - 1]] + v[i - 1])
        m[1,c] = m[2, c]
        if c >= w[0]:
            m[1, c] = max(m[1, c], m[2, c - w[0]] + v[0])
    x = np.zeros(n + 1 , dtype = np.int)
    trackback(m, w, c, n ,x)

def trackback(m, w, c, n, x):
    for i in range(1, n):
        if m[i, c] ==  m[i + 1, c]:
            x[i] = 0
        else:
            x[i] = 1
            c = c - w[i - 1]
    x[n] = 1 if m[n,c] > 0 else 0
    k = [n for n in range(n + 1) if x[n] != 0]
    for i in k:
        print(i, end=' ')
def main():
    c = int(input())
    n = int(input())
    v = np.array(input().split(), dtype = np.int)
    w = np.array(input().split(), dtype = np.int)
    knapsack(v, w, c, n)

if __name__ == '__main__':
    main()

"""
10
5
6 3 5 4 6
2 2 6 5 4
"""