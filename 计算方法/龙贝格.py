import numpy as np
import math
def main():
    n = int(input())
    romber(0, math.pi / 2, n )

def f(x):
    return (x * x + x + 1)*np.cos(x)

def romber(a, b, n):
    tol = np.finfo(np.float32).eps
    M = 1
    h = b - a
    err = 1
    J = 0
    R = np.zeros((7, 7), dtype=np.double)
    R[1, 1] = h * (f(a) + f(b)) / 2
    while ((err >tol) and( J < n)) or J < 4:
        J = 1 + J
        h = h / 2
        s = 0
        for p in range(1,M + 1):
            x = a + h* (2 * p- 1)
            s = s + f(x)
        R[J+1, 1] = R[J, 1] / 2 + h * s
        M = 2 * M
        for k in range(1, J + 1):
            R[J + 1, k + 1] = R[J + 1, k] + (R[J + 1, k]- R[J, k]) / (4 **k - 1)
            err = np.abs(R[J ,J] - R[J + 1, k + 1])
    print(R[1:,1:5])

if __name__ == '__main__':
    main()