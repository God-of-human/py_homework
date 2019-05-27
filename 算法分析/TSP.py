"""
首先构造解空间树，然后深度优先遍历
open表是一个先进后出的队列，遍历解空间树时，把生成的满足条件的子节点倒序加入队列中
经过观察得到，每弹出一个节点，此时路径即为该节点到跟节点的路径
当弹出节点的cost值大于best_cost时，即终止继续深入
"""
import numpy as np
import queue as qu

class VertexNode():
    def __init__(self, index = None, cost = 0 , previous = None):
        self.index = index
        self.cost = cost
        self.previous = previous
    def __repr__(self):
        return "<Vertex '{} 'with cost '{}'> ".format(self.index, self.cost)
    #重定义运算符， 为了队列的排序
    def __lt__(self, other):
        return self.cost < other.cost

def tsp(adj_list, s_index):
    n = len(adj_list)
    best_cost = np.inf
    #创建队列
    open = qu.LifoQueue()
    Q = VertexNode(s_index - 1)
    open.put(Q)
    #best_path：用来记录最优路径
    best_path = []
    while not open.empty():
        u = open.get()
        #path记录当前路径
        path = []
        #如果此时的节点到根路径的cost比best大
        k = u
        #构建路径，从当前节点回溯，然后倒序输出
        while k.previous != None:
            path.append(k.index+1)
            k = k.previous
        path.append(1)
        #输出路径
        print(path[::-1])
        #用path的长度来判断是否到达叶节点
        if len(path) == n:
            #u_cost 记录当前节点到根节点的路径的cost之和，加上到叶节点到根节点的cost
            if u.cost + adj_list[u.index][0] <  best_cost:
                best_cost = u.cost + adj_list[u.index][0]
                best_path = path
        #如果不是叶节点
        else:
            list = []
            if u.cost >= best_cost:
                continue
            for key in adj_list[u.index]:
                list.append(key)
            #生成的节点倒序加入open队列
            for i in reversed(list):
                if i+1 not in path:
                    m = VertexNode(i)
                    #生成节点的前节点是当前节点
                    m.previous = u
                    m.cost = adj_list[u.index][i] + u.cost
                    if m.cost < best_cost:
                        open.put(m)
    print("{}: {}".format(best_cost,best_path[::-1]))

def main():
    n = int(input())
    #创建邻接表
    adj_list = [{}]*n
    for i in range(n):
        temp = np.array(input().split(), dtype = np.int)
        temp_dict = {}
        for k in range(len(temp)):
            if temp[k] != 0:
                temp_dict.setdefault(k, temp[k])
        adj_list[i] = temp_dict
    s_index = 1
    tsp(adj_list,s_index)

if __name__ == '__main__':
    main()


"""
4
0 30 6 4
30 0 5 10
6 5 0 20
4 10 20 0
"""