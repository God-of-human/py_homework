"""
1:利用字符集中每个字符的使用频率作为权值构造一个Huffman tree
2：从根节点开始，为到每个节点路径上的左分支赋值0，右分支赋值1，并从根到叶子方向形成该叶子节点的编码
"""
class Node(object):
    def __init__(self,name=None,value=None):
        self._name=name
        self._value=value
        self._left=None
        self._right=None

#哈夫曼树类
class HuffmanTree(object):

    #根据Huffman树的思想：以叶子节点为基础，反向建立Huffman树
    def __init__(self,char_weights):
        self.a=[Node(part[0],part[1]) for part in char_weights]  #根据输入的字符及其频数生成叶子节点
        while len(self.a)!=1:
            self.a.sort(key=lambda node:node._value,reverse=True)
            c=Node(value=(self.a[-1]._value+self.a[-2]._value))
            c._left=self.a.pop(-1)
            c._right=self.a.pop(-1)
            self.a.append(c)
        self.root=self.a[0]
        self.b= [i for i in range(10)]    #self.b用于保存每个叶子节点的Haffuman编码,range的值只需要不小于树的深度就行
        self.code = [i for i in range (len(char_weights))]

    #用递归的思想生成编码
    def pre(self,tree,length):
        node=tree
        if (not node):
            return
        elif node._name:
            k = ord(node._name) - 97
            code = ""
            for i in range(length):
                m = str(self.b[i])
                code += m
            self.code[k] = code
            return
        self.b[length]=0
        self.pre(node._left,length+1)
        self.b[length]=1
        self.pre(node._right,length+1)
     #生成哈夫曼编码
    def get_code(self):
        self.pre(self.root,0)
        for i in range(len(char_weights)):
            print(chr(i + 97),end=" ")
            print(self.code[i])

if __name__=='__main__':
    #输入的是字符及其频数
    n = int(input())
    list = list(input().split())
    char_weights = []

    for i in range(n):
        item = []
        c = chr(i + 97)
        x = (list[i])
        item.append(c)
        item.append(int(x))
        x = tuple(item)
        char_weights.append(x)
    tree=HuffmanTree(char_weights)
    tree.get_code()
