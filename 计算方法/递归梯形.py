"""
根据书上的公式，及代码，完成作业
"""
import numpy as np

#定义函数
def f(x):
    return 1/x

def main():
    # X 依次代表积分上限、下限 和迭代次数
    X = np.array(input().split(), dtype=np.int)
    #调用函数
    rctrap(X[0], X[1], X[2])
def rctrap(a, b, n):
    M = 1
    h = b - a
    #T代表积分近似值
    T = np.zeros((n + 1,1), dtype=np.double)
    T[0] = h * (f(a) + f(b)) / 2
    for j in range(n):
        M = 2 * M
        h = h / 2
        s = 0
        for k in range(int(M/2)):
            x = a + h * (2 * (k + 1) -1)
            s = s + f(x)
        T[j + 1] = T[j] / 2 + h * s

    print(T)

if __name__ == '__main__':
    main()