"""
问题描述】考虑[0.0,1.2]内的函数y=f(x)=cos(x)。利用多个（2,3,4等）节点构造拉格朗日插值多项式。
【输入形式】在屏幕上依次输入在区间[0.0,1.2]内的一个值x*，构造插值多项式后求其P(x*)值，和多个节点的x坐标。
【输出形式】输出插值多项式系数矩阵，拉格朗日系数多项式矩阵和P(x*)值（保留小数点后6位有效数字）。
【样例1输入】
0.3
0 1.2
【样例1输出】
[-0.53136854  1.        ]
[[-0.83333333  1.        ]
 [ 0.83333333  0.        ]]
P1(0.3)=0.840589
"""
import numpy as np
import math
def lagran(X, Y, x):
    w = X.size
    #L 拉格朗日系数多项式矩阵
    # C 插值多项式矩阵
    L = np.zeros((w, w), dtype=np.float64)
    n = w - 1
    for k in range(n + 1):
        V = 1
        for j in range(n + 1):
            if(k != j):
                V = np.convolve(V,np.poly(X[j])) / (X[k] - X[j])
        L[k,:] = V
    C = Y @ L
    print(C)
    print(L)
    # a = np.poly1d(C)
    # print(a)
    result = np.polyval(C ,x)
    i = w - 1
    print("P{}({})={:.6}".format(i, x, result))



def main():
    x = float(input())
    #X输入的点
    X = np.array(input().split(), dtype=float)
    length = X.size
    #Y，每个点对应的结果
    Y = np.zeros(length, dtype=np.float64)
    for i in range(length):
        Y[i] = np.cos(X[i])
    lagran(X,Y, x)


if __name__ == '__main__':
    main()