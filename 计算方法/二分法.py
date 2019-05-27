"""
【输入形式】在屏幕上输入3个数，分别表示左端点值、右端点值和精确到小数点后的位数。各数间都以一个空格分隔。
【输出形式】第一行输出迭代次数，第二行输出利率（精确到小数点后11位）
【样例输入】
  0.15 0.16 10
【样例输出】

  27

  0.15753931027
"""
import numpy as np
def Calcu(I):
    sum = 300 / I * 12 * ((1 + I / 12) ** 240 - 1)
    return sum

def main():
    X = np.array(input().split(),dtype = np.float)
    a1 = X[0]
    a2 = X[1]
    count = 0
    a3 = int(X[2])
    des = float(10 ** (-a3))
    #确定精度
    while abs(a2-a1) >= des:
        count += 1
        I = (a1+a2)/2
        if Calcu(I) - 500000 > 1E-11:
            a2 = I
        elif Calcu(I) - 500000 < -1E-11:
            a1 = I
    print(count)
    print("%.11f"%((a1+a2)/2))

if __name__ == '__main__':
    main()

