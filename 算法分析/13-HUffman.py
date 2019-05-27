import numpy as np
import heapq as hq

class Node:
    left = None     # 左节点
    right = None    # 右结点   

    # 初始化结点
    def __init__(self, v=0, sym='.'):
        self.value = v      # 权值
        self.word = sym     # 所代表的字母，默认为 '.'

    # 重定义运算符 < 当对类对象使用小于号的时候，会调用这个函数
    def __lt__(self, other):
        return self.value < other.value


def main():
    # 获取输入
    n = int(input())
    freq_array = np.array(input().split(), int)

    # 创建最小堆
    min_heap = []
    for i in range(n):
        min_heap.append(Node(freq_array[i], chr(ord('a') + i)))
    # min_heap = [Node(freq_array[i], chr(ord('a') + i)) for i in range(n)]

    hq.heapify(min_heap)

    # 循环
    for i in range(n - 1):
        temp_node = Node()
        temp_node.left  = hq.heappop(min_heap)
        temp_node.right = hq.heappop(min_heap)
        temp_node.value = temp_node.left.value + temp_node.right.value
        hq.heappush(min_heap, temp_node)
    # 得到结果
    result = {}
    encode(min_heap[0], '', result)
    # 输出
    for i in range(n):
        index = chr(ord('a') + i)
        print(chr(ord('a') + i), result[index])


def encode(nodes, code, res):
    # 深度优先遍历
    if nodes.left:
        encode(nodes.left , code+'0', res)
    if nodes.right:
        encode(nodes.right, code+'1', res)

    # 存到结果字典里
    if not nodes.left and not nodes.right:
        res[nodes.word] = code      # {···， nodes.word : code, ···}

if __name__ == '__main__':
    main()