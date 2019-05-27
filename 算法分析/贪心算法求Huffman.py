"""
贪心算法求Huffman树，我觉得关键的一句话：自底向上构建，由叶子节点开始，根据Huffman树的定义设计算法，
用类的方法构建节点结构体，用递归构建编码
"""
# 构建节点，self.isin代表是否加入列表
class Node():
    def __init__(self, value):
        self.value = value
        self.isin = False
        self.left = None
        self.right = None

class Huffman():
# 构建Huffmans
#m1是右端点，m2是左左端点
    def __init__(self,l):
        self.list = []
        for i in range(0, len(l)):
            self.list.append(Node(l[i]))
        k = Node(float('inf'))
        while len(self.list) < 2 * len(l) - 1:
            m1 = m2 = k
            for x in range (0, len(self.list)):
                self.list[x].value = float(self.list[x].value)
                if m1.value > self.list[x].value and (self.list[x].isin is False):
                    m2 = m1
                    m1 = self.list[x]
                elif m2.value > self.list[x].value and (self.list[x].isin is False):
                    m2 = self.list[x]
            H = Node(m1.value + m2.value)
            H.right = m1
            H.left = m2
            # self.list.pop(-1)
            # self.list.pop(-1)
            self.list.append(H)
            m1.isin = m2.isin = True
            self.root = H
        self.b = [i for i in range(10)]  #用于保存每个叶子节点的Huffman编码
    def pre(self,tree,length):
        node = tree
        if (not node):
            return
        elif node.value:
            for i in range(length):
                print(self.b[i],end=' ')
            print()
            #return
        self.b[length] = 0
        self.pre(node.left, length + 1)
        self.b[length] = 1
        self.pre(node.right, length + 1)

    def get_code(self):
        self.pre(self.root,0)

def main():
    n = int(input())
    p =list(input().split())
    tree = Huffman(p)
    tree.get_code()

if __name__=='__main__':
    main()

