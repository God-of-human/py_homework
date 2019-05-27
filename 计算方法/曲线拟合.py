import numpy as np

def lspoly(M, m):
    B = np.zeros((1, 3),dtype=np.float64)
    X = M[:, 0]
    n = X.size
    F = np.zeros((n, 3), dtype=np.float64)
    Y = M[:, 1]
    for i in range(3):
        F[:, i] = X**(i)
    A = F.T @ F
    B = F.T @ Y
    C = np.linalg.solve(A, B)
    C = np.flipud(C)
    result = np.zeros(m,dtype=np.float64)
    for i in range (m):
        result[i] = np.polyval(C,X[i])
    err = np.linalg.norm(result - Y)
    print(C)
    print("{:.7}".format(err))



def main():
    m = int(input())
    M = np.zeros((m,2), dtype=np.float64)
    for i in range(m):
        M[i, :] = np.array(input().split(), dtype = np.float64)
    lspoly(M, m)
if __name__ == '__main__':
    main()


'''
4
-3 3
0 1
2 1
4 3
'''
"""
5
0. 0.1
0.25 0.35
0.5 0.81
0.75 1.09
1. 1.96
"""