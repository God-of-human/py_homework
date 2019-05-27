"""
	牛顿插值多项式（插值法）
【问题描述】考虑[0,4]内的函数y=f(x)=cos(x)。利用多个（2,3,4等）节点构造牛顿插值多项式。
【输入形式】在屏幕上依次输入在区间[0,4]内的一个值x*，构造插值多项式后求其P(x*)值，和多个节点的x坐标。
【输出形式】输出牛顿插值多项式系数向量，差商矩阵和P(x*)值（保留小数点后6位有效数字）。
【样例1输入】
0.3
0 1 2 3 4
"""
import numpy as np

def newpoly(X,Y,x):
    n = X.size
    #D代表差商
    D = np.zeros((n, n), dtype=np.double)
    D[:,0] = Y[:]
    #a代表最高次
    a = n - 1
    #j 代表第几列
    for j in range(1, n):
        #k，代表第几行
        for k in range(j, n):
            D[k, j] = (D[k, j - 1] - D[k  - 1, j - 1])/(X[k] - X[k - j])
    C = D[n - 1, n - 1]
    for k in range(n-2, -1, -1):
        C = np.convolve(C, np.poly(X[k]))
        #因为此时C是一个一维数组，所以才可以用size，size在我看来表达的是，矩阵中元素的个数。
        m = C.size
        #这个是符合嵌套乘法，C的最后一个是一个常数项。
        C[m - 1] = C[m - 1] + D[k, k]
    #fomula 代表的是该多项式
    fomula = np.poly1d(C)
    #计算该多项式。
    result = np.polyval(fomula, x)
    print(fomula)
    print(D)
    print('P{}({})={:.6}' .format(a, x, result))
def main():
    x = float(input())
    #X代表横坐标
    X = np.array(input().split(), dtype=np.float)
    length = X.size
    #Y代表纵坐标
    Y = np.zeros(length, dtype=np.float)
    for i in range(length):
        Y[i] = np.cos(X[i])
    newpoly(X, Y, x)
if __name__ =='__main__':
    main()


