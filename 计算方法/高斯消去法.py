"""
	高斯消去法（线性方程组求解）
【问题描述】为求解一个线性方程组，首先构造增广矩阵[A|B]，采用偏序选主元策略的高斯消去法变换成上三角矩阵，再执行回代过程得到解。
【输入形式】在屏幕上依次输入方阵阶数n，系数矩阵A和常数矩阵B。
【输出形式】每一行输出X的一个解。
【样例1输入】
4
1 2 1 4
2 0 4 3
4 2 2 1
-3 1 3 2
13
28
20
6
"""

import numpy as np

def upper_triangular(a, b):
    #epsilon表示一个极小值，用来判定奇异矩阵
    epsilon = np.finfo(np.float32).eps
    #n 代表b的长度
    n = b.size
    #aug是增广矩阵
    aug = np.hstack((a, b))
    #对每一行进行操作
    for p in range(n):
        temp = aug[p:, p]
        #返回最大数的索引，默认情况下，索引是平铺的数组，axis = 0， 代表列
        # = 1代表行
        max_index = np.argmax(np.abs(temp))
        max_row = max_index + p
        #交换行
        aug[[p, max_row], : ] = aug[[max_row, p], :]
        #aug[p, p] != 0, 如果条件不满足，则可能无解或有无穷解
        if aug[p, p] < epsilon:
            print("Array was singular")
            break
        #高斯消去，就是平时解矩阵的方法，转化为上三角矩阵。
        for k in range(p + 1, n):
            #m 是倍数
            m = aug[k, p] / aug[p, p]
            aug[k, p] = 0
            aug[k, p + 1:] = aug[k, p + 1:] - m * aug[p, p + 1:]
    #回代法求矩阵的解
    x = backsub(aug[:, :-1], aug[:,-1])

    return x

def backsub(a, b):
    n = b.size
    x = np.zeros([n, 1], dtype=np.double)
    #Xn 的解
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    #循环使用回代法，倒序
    for k in range (n - 2, -1, -1):
        x[k] = (b[k] - a[k, k + 1:] @ x[k + 1 :]) / a[k, k]
    return x


def main():
    #n 矩阵阶数
    n = int(input())
    a = np.zeros((n , n), dtype = np.double)
    #输入系数矩阵
    for r in range (n):
        a[r, :] = np.array(input().split(), dtype = np.double)
    #输入常数矩阵
    b = np.zeros((n, 1), dtype = np.double)
    for r in range (n):
        b[r] = np.array(input().split(), dtype = np.double)
    #调用函数
    x = upper_triangular(a, b)
    print(x)

if __name__ == '__main__':
    main()