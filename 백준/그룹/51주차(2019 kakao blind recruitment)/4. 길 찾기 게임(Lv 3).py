import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, index=None, node=None):
        self.left = None
        self.right = None
        self.index = index
        self.node = node


class Tree:
    def __init__(self, ):
        self.root = None

    def insert(self, index, info):
        if self.root == None:
            self.root = Node(index, info)
        else:
            self.tmp = self.root
            while True:
                if info < self.tmp.node:  # left
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

    def prefix(self, node, answer):
        if node == None:
            return answer

        answer.append(node.index)
        self.prefix(node.left, answer)
        self.prefix(node.right, answer)

        return answer

    def postfix(self, node, answer):
        if node == None:
            return answer

        self.postfix(node.left, answer)
        self.postfix(node.right, answer)
        answer.append(node.index)

        return answer


def solution(nodeinfo):
    answer = [[]]

    node_index = {}
    for id, node in enumerate(nodeinfo, 1):
        node_index[node[0]] = id

    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    tree = Tree()
    for node in nodeinfo:
        tree.insert(node_index[node[0]], node[0])  # node의 번호, node의 x좌표

    prefix = tree.prefix(tree.root, [])
    postfix = tree.postfix(tree.root, [])

    answer = [prefix, postfix]

    return answer