import numpy as np
import heapq as hq

class Vertex:
    def __init__(self, index = None, dist = np.inf, pre = None):
        self.index = index
        self.dist = dist
        self.pre = pre

    def __repr__(self):
        return " <vertex '{}' with distance '{}'>".format(self.index, self.dist)

    def __lt__(self, other):
        return self.dist < other.dist

def dijkstra(adj_list, s_index):
    n = len(adj_list)
    min_heaq = [Vertex(index=i) for i in range(n)]
    min_heaq[s_index - 1].dist = 0
    hq.heapify(min_heaq)
    s_dict = {}
    while len(min_heaq):
        u = hq.heappop(min_heaq)
        s_dict.setdefault(u.index, u)
        for k in adj_list[u.index]:
            for i in range(len(min_heaq)):
                if k == min_heaq[i].index and min_heaq[i].dist > u.dist:
                    min_heaq[i].pre = u
                    min_heaq[i].dist = u.dist + adj_list[u.index][k]
                    hq.heapify(min_heaq)
    return s_dict
def showpath(s_dict):
    for i in range(1, len(s_dict)):
        print("{}: ".format(s_dict[i].dist), end="")
        s = ""
        k = s_dict[i]
        while k.pre != None:
            s = "->"  + str(k.index + 1) + s
            k = k.pre
        print("1" + s)

def main():
    n = int(input())
    adj_list = [{}] * n
    for k in range(n):
        temp = np.array(input().split(), dtype=np.int8)
        temp_list = {}
        for i in range (len(temp)):
            if temp[i] != 0:
                temp_list.setdefault(i, temp[i])
        adj_list[k] = temp_list
    s_index = 1
    s_dict = dijkstra(adj_list, s_index)
    #按照字典中的key值（顶点序号进行排序）
    showpath(s_dict)
    s_index_sorted_list = sorted(s_dict.items(), key = lambda x:x[0])
    print(s_index_sorted_list)

if __name__ == '__main__':
    main()



"""
5
0 10 0 30 100
0 0 50 0 0
0 0 0 0 10
0 0 20 0 60
0 0 0 0 0
"""