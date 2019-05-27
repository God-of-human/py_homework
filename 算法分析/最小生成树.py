"""
【问题描述】Prim算法解决的是带权重的无向图上连接所有顶点的耗费最小的生成树。
【输入形式】在屏幕上输入顶点个数和连接顶点间的边的权矩阵。
【输出形式】从源到各个顶点的最短距离及路径。
【样例输入】
8
0 15 7 0 0 0 0 10
15 0 0 0 0  0 0 0
7 0 0 9 12 5 0 0
0 0 9 0 0 0 0 0
0 0 12 0 0 6 0 0
0 0 5 0 6 0 14 8
0 0 0 0 0 14 0 3
10 0 0 0 0 8 3 0
【样例输出】
15: 1<-2
7: 1<-3
9: 1<-3<-4
6: 1<-3<-6<-5
5: 1<-3<-6
3: 1<-3<-6<-8<-7
8: 1<-3<-6<-8
"""
import numpy as np
import heapq as hq

#定义节点类
class Vertex():
    def __init__(self, index = None, pre = None, value = np.inf):
        self.index = index
        self.value = value
        self.pre = pre

    def __repr__(self):
        return "<vertex {} with value {}".format(self.index, self.value)

    def __lt__(self, other):
        return self.value < other.value


def prim(adj_list, s_index):
    n = len(adj_list)
    min_heaq = [Vertex(index = i) for i in range(n)]
    min_heaq[s_index - 1].value = 0
    hq.heapify(min_heaq)
    dict = {}
    while len(min_heaq):
        u = hq.heappop(min_heaq)
        dict.setdefault(u.index, u)
        for k in adj_list[u.index]:
            for i in range(len(min_heaq)):
                if k == min_heaq[i].index and min_heaq[i].value > adj_list[u.index][k]:
                    min_heaq[i].pre = u
                    min_heaq[i].value = adj_list[u.index][k]
                    hq.heapify(min_heaq)
    return dict

def showpath(s_dict):
    for i in range(1, len(s_dict)):
        print("{}:".format(s_dict[i].value), end="")
        k = s_dict[i]
        s = ""
        while k.pre != None:
            s = "<-" + str(k.index + 1) + s
            k = k.pre
        print("1" + s)


def main():
    #输入节点
    n = int(input())
    #创建linjieb
    adj_list = [{}] * n
    for i in range(n):
        temp_list = {}
        temp = np.array(input().split(), dtype=np.int)
        for k in range(len(temp)):
            if temp[k] != 0:
                temp_list.setdefault(k, temp[k])
        adj_list[i] = temp_list
    s_index = 1
    s_dict = prim(adj_list, s_index)
    showpath(s_dict)

if __name__=='__main__':
    main()