"""
【问题描述】组合辛普森公式求f(x)=2+sin(2*sqrt(x))的积分近似值。
【输入形式】在屏幕上依次输入积分上限、下限和等距子区间个数。
【输出形式】输出使用组合辛普森公式求得的积分近似值。
【样例1输入】
1 6 5
【样例1输出】
8.18301549
"""
import numpy as np
# 定义f（x）
def f(x):
    y = 2 + np.sin(2 * x**(0.5))
    return y

def simprl(a, b, m):
    h = (b - a) / (2 * m)
    s1 = 0
    s2 = 0
    for k in range(m):
        x = a + h * (2*(k + 1) - 1)
        s1 = s1 + f(x)
    for k in range(m -1):
        x = a + h * 2 * (k + 1)
        s2 = s2 + f(x)
    s = h * (f(a) + f(b) + 4 * s1 +2 * s2) / 3
    print("%.8f"% s)


def main():
    li = np.array(input().split(), dtype = np.int8)
    simprl(li[0], li[1], li[2])

if __name__ == '__main__':
    main()
