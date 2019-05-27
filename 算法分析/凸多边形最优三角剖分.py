import numpy as np

def minWeightTriangulation(n,coordinate):
    t = np.zeros((n, n ), dtype=np.float32)
    s = np.zeros((n , n), dtype=np.int32)
    for len in range (2, n):
        for i in range (1, n - len + 1):
            j = i + len - 1
            t[i,j] = np.inf
            s[i][j] = i
            for k in range (i, j):
                q = t[i, k] + t[k + 1, j] + distance(coordinate[i - 1], coordinate[k], coordinate[j])
                if q < t[i, j]:
                    t[i, j] = q
                    s[i, j] = k
    back(1,n - 1, s)
def back(i, j, s):
    if i == j:
        return
    back(i, s[i][j],s)
    back(s[i][j] + 1, j, s)
    print(i - 1,end='')
    print(s[i][j],end='')
    print(j)

def distance(x, y, z):
    d1 = np.linalg.norm(x - y)
    d2 = np.linalg.norm(x - z)
    d3 = np.linalg.norm(z - y)
    return d1 + d2 + d3

def main():
    n = int(input())
    coordinate = np.zeros((n,2), dtype=np.float32)
    for i in range(n):
        coordinate[i,:] = np.array(input().split(),dtype=np.float)
    minWeightTriangulation(n, coordinate)

if __name__ == '__main__':
    main()