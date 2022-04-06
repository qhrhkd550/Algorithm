'''
* 문제 유형 : 이진 트리

* 체감 난이도 : ****

* 아이디어 1
  - 이진트리를 구현하면 쉽게 해결
  - 단, 파이썬의 경우 recursionlimit를 늘려야한다.
'''
import sys
sys.setrecursionlimit(1006)

class Node:
    def __init__(self, index=None ,node=None):
        self.left = None
        self.index = index
        self.node = node
        self.right = None
        
        
class Tree:
    def __init__(self, ):
        self.root = None
    
    def insert(self, index, info): # (index, (x, y))
        if self.root == None:
            self.root = Node(index, info)
        else:
            self.tmp = self.root
            while True:
                if info < self.tmp.node:
                    if self.tmp.left != None:
                        self.tmp = self.tmp.left
                    else:
                        self.tmp.left = Node(index, info)
                        break
                        
                elif info > self.tmp.node:
                    if self.tmp.right != None:
                        self.tmp = self.tmp.right
                    else:
                        self.tmp.right = Node(index, info)
                        break
    
    def preorder(self, node, answer): # node left right
        if node == None:
            return answer
        answer.append(node.index) 
        self.preorder(node.left, answer)
        self.preorder(node.right, answer)
        
        return answer
        
        
    def postorder(self, node, answer):
        if node == None:
            return answer
        self.postorder(node.left, answer)
        self.postorder(node.right, answer)
        answer.append(node.index) 
        
        return answer
        
from collections import defaultdict

def solution(nodeinfo):
    
    node_index = defaultdict(int)
    for i, node in enumerate(nodeinfo, 1):
        node_index[node[0]] = i
        
    nodeinfo = sorted(nodeinfo, key=lambda x : (-x[1], x[0]))
    
    tree = Tree()
    for x, y in nodeinfo:
        tree.insert(node_index[x], x)
        
    a = tree.preorder(tree.root, [])
    b = tree.postorder(tree.root, [])

    return [a, b]
