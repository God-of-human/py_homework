"""
递归结构
1：当xm = yn时，找出Xm-1和Yn-1的最长公共子序列，然后在其尾部加上xm （或yn ）；

2：当xm ≠ yn时，必须解两个子问题：
找出Xm-1和Y的最长公共子序列及 X和Yn-1的最长公共子序列
这两个公共子序列中较长者即为X和Y的最长公共子序列。
"""
import numpy as np

def LCSLength(X, Y, m, n):
    b = np.zeros((m + 1, n + 1), dtype=np.int)
    c = np.zeros((m + 1, n + 1), dtype=np.int)
    #c[i, j]记录两个序列最长公共字序列的长度
    for i in range(1, m + 1):
        c[i, 0] = 0
    for j in range(0, n + 1):
        c[0, j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 1
                b[i, j] = 1
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]
                b[i, j] = 2
            else:
                c[i, j] = c[i, j - 1]
                b[i, j] = 3
    print(c)
    return b


def LCS(b, X, i, j ):
    if i == 0 or j == 0:
        return
    if b[i, j] == 1:
        LCS(b, X, i - 1, j - 1)
        print(X[i - 1], end='')
    elif b[i, j] == 2:
        LCS(b, X, i - 1, j)
    else:
        LCS(b, X, i, j - 1)

def main():
    X = np.array(input().split())
    Y = np.array(input().split())
    m = X.size
    n = Y.size
    b = LCSLength(X, Y, m, n)
    LCS(b, X, m, n)


if __name__ == '__main__':
    main()



"""
A B C B D A B
B D C A B A
"""
""""
输出：
[[0 0 0 0 0 0 0]
 [0 0 0 0 1 1 1]
 [0 1 1 1 1 2 2]
 [0 1 1 2 2 2 2]
 [0 1 1 2 2 3 3]
 [0 1 2 2 2 3 3]
 [0 1 2 2 3 3 4]
 [0 1 2 2 3 4 4]]

 BCBA
"""