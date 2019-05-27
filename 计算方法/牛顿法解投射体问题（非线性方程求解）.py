"""
问题描述】在考虑空气阻力情况下，
求解投射体撞击地面时经过的时间和水平飞行行程，
其中：y=f(t)=9600*(1-e**(-t/15.0)) - 480*t；x=r(t)=2400*(1-e**(-t/15.0))。
【输入形式】在屏幕上输入3个数，分别表示起始值、
前后两次迭代的差的绝对值精度和函数值的精度。各数间都以一个空格分隔
"""
import numpy as np

 #原函数
def height(t):
    return 9600*(1 - np.exp(-t / 15.0)) - 480*t

def distance(t):
    return 2400*(1 - np.exp( -t / 15.0))

#导函数
def dheight(t):
    return 9600 * (1/15.0) * np.exp(-t / 15.0) - 480

def number_to_sci(x):
    #由精确到小数点的位数得到科学技术值
    switcher = {
        1.0: 1E-1,
        2.0: 1E-2,
        3.0: 1E-3,
    }
    return switcher.get(x,"nothing")

def iter(p0, err, epsilon):
    max_iter = 0
    #输入的是精度位数，比如精确到小数点后一位，后两位，
    # 这里是把位数转化为具体的小数点后几位
    err2 = number_to_sci(err)
    epsilon2 =number_to_sci(epsilon)
    #max_iter表示最大的迭代次数
    while max_iter < 50:
        #每迭代一次，就向根靠近一点，p0代表经过的时间，就是根
        p1 = p0 - height(p0) / dheight(p0)
        #err1表示误差
        err1 = np.abs(p1 - p0)
        p0 = p1
        #相对误差
        rel_err = err1 / (np.abs(p1) +epsilon)
        #y表示高度，当低于一定的高度的时候，即接近于0，表示物体已经降落到地上。
        y = height(p0)
        #epsilon2表示函数值的精度。函数高的精度
        if(err1 < err2 or np.abs(y) < epsilon2 or rel_err <err2):
            break
    print('%.5f' % p0)
    print('%.5f' % distance(p0))

def main():
    #输入3个数，分别表示起始值，前后两次迭代的差的绝对值精度和函数值的精度
    li = list(map(int, input().split()))
    array = np.array(li, dtype=int)
    iter(array[0], array[1], array[2])

if __name__ == '__main__':
    main()
