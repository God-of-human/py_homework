import numpy as np

def lsline(X,n):
    #对各列求均值,axis = 0, 对列，axis = 1 对行
    mean = np.mean(X, axis=0)
    sum2 = 0
    sumxy = 0.0
    b = np.zeros(2, dtype=np.float32)
    for i in range (n):
        sum2 = sum2 + (X[i,0] - mean[0])*(X[i, 0] - mean[0])
        m = X[i, 0] - mean[0]
        sumxy = sumxy + (X[i, 1] - mean[1])*(X[i, 0] - mean[0])
    b[0] = sumxy / sum2
    b[1] = mean[1] - b[0] * mean[0]
    resultarray = np.zeros((n, 2), dtype=np.float64)
    for i in range(n):
        resultarray[i,:] = np.array((X[i, 0], np.polyval(b, X[i, 0])))
    #b = np.around(b, 8)
    print("y={:.7f}x+{:.7f}".format(b[0],b[1]))
    err = np.linalg.norm(X - resultarray)
    err = np.around(err, 7)
    print(err)
def main():
    n = int(input())
    X = np.zeros((n, 2), dtype=np.float64)
    for i in range(n):
        X[i, :] = np.array(input().split())
    lsline(X,n)

if __name__ == '__main__':
    main()