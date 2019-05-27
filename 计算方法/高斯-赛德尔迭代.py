import numpy as np

def gseid(A, B, P, delta, max1):
    eps = np.finfo(np.float32).eps
    N = B.size
    X = np.zeros((N, 1), dtype=np.double)
    count = 0
    for k in range(max1):
        for j in range(N):
            if j == 0:
                X[0] = (B[0] - A[0, 1:N] @ P[1:N]) / A[0,0]
            elif j == N:
                X[N] = (B[N] - A[N, 0:N - 1] @ X[0:N - 1]) / A[N, N]
            else:
                X[j] = (B[j] - (A[j, 0:j] @ P[0:j] + A[j, j + 1:] @ P[j + 1:])) / A[j, j]
            err = np.abs(np.linalg.norm(X - P))
            relerr = err / (np.linalg.norm(X) + eps)
            P[:] = X[:]

        if err < delta or relerr < delta:
            break
        count += 1
    print(count)
    print(X)


def main():
    n = int(input())
    A = np.zeros((n, n), dtype=np.double)
    for r in range(n):
        A[r, :] = np.array(input().split(),dtype=np.double)
    B = np.zeros((n, 1), dtype=np.double)
    P = np.zeros((n, 1), dtype=np.double)
    for r in range(n):
        B[r] = np.array(input().split(), dtype=np.double)
    for r in range(n):
        P[r] = np.array(input().split(), dtype=np.double)
    max1 = 20
    delta = 1E-9
    gseid(A, B, P,delta, max1)

if __name__ == '__main__':
    main()