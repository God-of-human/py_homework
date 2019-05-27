"""
【问题描述】组合梯形公式求函数f(x)=2+sin(2*sqrt(x))的积分近似值。
【输入形式】在屏幕上依次输入积分上限、下限和等距子区间个数。
【输出形式】输出使用组合梯形公式求得的积分近似值。
【样例1输入】
1 6 10
【样例1输出】
8.19385457
"""
import numpy as np

# 定义f（x）
def f(x):
    y = 2 + np.sin(2 * x**(0.5))
    return y

def traprl(a, b, m):
    h = (b - a) / m
    s =0
    for k in range(m - 1):
        x = a + h *(k + 1)
        s = s + f(x)
    s = h * (f(a) + f(b)) / 2 + h * s
    print("%.8f"% s)


def main():
    li = np.array(input().split(), dtype = np.int8)
    traprl(li[0], li[1], li[2])

if __name__ == '__main__':
    main()
