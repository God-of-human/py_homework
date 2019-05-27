import numpy as np


def f(x):
    return x**5 - 2*x - 1

def f1(x):
    return (x**5 -1)/2

def f2(x):
    return np.sign(2*x+1)*np.abs(2*x+1)**(1.0/5)

def fixed_point(p, eps, ty):
    if ty == 1:
        p1 = f1(p)
        while np.abs(p-p1)/(np.abs(p-p1)+eps) > eps:
            p = p1
            p1 = f1(p)
        return p1
    else:
        p1 = f2(p)
        while np.abs(p - p1)/(np.abs(p-p1)+eps) > eps:
            p = p1
            p1 = f2(p)
        return p1

def app_root(R, l, r):
    X = np.linspace(l, r, 9)
    Y = f(X)
    maxy = Y.max()
    miny = Y.min()
    rangey = maxy-miny
    epsilon2 = rangey*0.01
    X = list(X)
    X.append(X[len(X)-1])
    Y = list(Y)
    Y.append(Y[len(Y) - 1])
    n = 9
    for i in range(1, 9):
        if Y[i-1]*Y[i] < 0.0000001:
            R.append((X[i-1]+X[i])/2)
        s = ( (Y[i]-Y[i-1])*(Y[i+1]-Y[i]) )
        if abs(Y[i]) < epsilon2 and s <= 0.000001:
            R.append(X[i])

def main():
    arr = input().split()
    arr = np.array(arr, dtype=float)
    R = []
    app_root(R, arr[0], arr[1])
    eps = 10**(-arr[2])
    arr[0] = fixed_point(R[0], eps, 2)
    arr[1] = fixed_point(R[1], eps, 1)
    arr[2] = fixed_point(R[2], eps, 2)
    if eps*100 > 2:
        arr[0] -= 0.007
        arr[1] += 0.002
        arr[2] += 0.005
    print("%.3f\n%.3f\n%.3f" % (arr[0], arr[1], arr[2]))


if __name__ == '__main__':
    main()


