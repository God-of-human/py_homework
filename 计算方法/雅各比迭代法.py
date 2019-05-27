"""
【问题描述】为求解一个线性方程组，使用雅可比迭代法，采用欧几里得距离判定是否收敛。精度delta为1E-9，最大迭代次数为20。

【输入形式】在屏幕上依次输入方阵阶数n，系数矩阵A，常数矩阵B和起始点P。

【输出形式】输出实际迭代次数，然后每一行输出一个根。

【样例1输入】
3
4 -1 1
4 -8 1
-2 1 5
7
-21
15
1
2
2
"""
import numpy as np

def jacobi(A, B, P, delta, max1):
    eps = np.finfo(np.float32).eps
    N = B.size
    count = 0
    X = np.zeros((N, 1), dtype=np.double)
    for k in range(max1):
        for j in range(N):
            X[j] = (B[j] - (A[j, 0:j]@P[0:j] + A[j, j + 1 :]@P[j + 1 :])) / A[j, j]
        err = np.abs(np.linalg.norm(X - P))
        #注意这个相对误差
        relerr = err / (np.linalg.norm(X) + eps)
        P[:] = X[:]
        if err < delta or relerr < delta :
            break
        count += 1
    print(count)
    print(X)

def main():
    n = int(input())
    A = np.zeros((n, n), dtype=np.double)
    for r in range(n):
        A[r, :] = np.array(input().split(),dtype=np.double)
    #B是常数矩阵
    B = np.zeros((n, 1), dtype=np.double)
    #P是起始点
    P = np.zeros((n, 1), dtype=np.double)
    for r in range(n):
        B[r] = np.array(input().split(), dtype=np.double)
    for r in range(n):
        P[r] = np.array(input().split(), dtype=np.double)
    max1 = 20
    delta = 1E-9
    jacobi(A, B, P,delta, max1)

if __name__ == '__main__':
    main()