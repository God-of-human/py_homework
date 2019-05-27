import numpy as np

def lutact(a, b):
    #高斯消去法求上三角矩阵
    epsilon = np.finfo(np.float32).eps
    n = b.size
    x = np.zeros([n, 1], dtype = np.double)
    y = np.zeros([n, 1], dtype = np.double)
    r = np.arange(n)
    for p in range(n):
        #基于偏序主元策略，换行
        temp = a[p:, p]
        max = np.argmax(np.abs(temp))       #数值最大的
        max_row = max + p                   #所在的行
        a[[p, max_row], :] = a[[max_row, p], :]
        r[p] , r[max_row] = r[max_row], r[p]
        if a[p, p] < epsilon:
            print("singlar")
            break
        for k in range(p + 1, n):
            m = a[k, p] / a[p, p]
            a[k, p] = m
            a[k, p + 1:] = a[k, p + 1:] - m*a[p, p + 1:]
    print(a)
    #前身替换法
    y[0] = b[r[0]]
    for k in range(1, n):
        y[k] = b[r[k]] - a[k, :k] @ y[:k]
    # 回代法
    x[n - 1] = y[n - 1] / a[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        x[k] = (y[k] - a[k, k + 1:] @ x[k + 1:]) / a[k, k]

    return x

def main():
    # 说明矩阵大小，输入系数矩阵和常熟矩阵
    n = int(input())
    a = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        a[i, :] = np.array(input().split(), dtype= np.double)
    #常数矩阵
    b = np.zeros((n, 1), dtype = np.double)
    for r in range(n):
        b[r] = np.array(input().split(), dtype=np.double)
    print(lutact(a, b))


if __name__ == '__main__':
    main()
