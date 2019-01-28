# https://www.welcomekakao.com/learn/courses/30/lessons/42892?language=python3
'''
binary search tree를 만들어서 travelsal을 하면 됨
문제에 주어진 모양을 만들기 위해 y값으로 정렬한 후 값을 insert하면 됨(처음에 있는 순서 그대로 insert할 경우 모양이 달라짐)
x,y 좌표 외에 node의 번호를 기억해야 함에 유의

*** 중요 ***
python 기본 call stack 제한이 1000이므로 recursion limit을 늘려주기 위해 다음의 코드가 필요함!
import sys
sys.setrecursionlimit(1500)
'''

import sys
sys.setrecursionlimit(1500)


class Node:
    LEFT = 0
    RIGHT = 1

    def __init__(self, val):
        self.val = val # (node_num, x)
        self.left = None
        self.right = None

    def add(self, val):
        if val[1] > self.val[1]:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.add(val)

        else:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.add(val)

    # return pre-order list
    def preorder(self):
        arr = [self.val] # root
        if self.left:
            arr.extend(self.left.preorder()) # left subtree
        if self.right:
            arr.extend(self.right.preorder()) # right subtree
        return arr

    def postorder(self):
        arr = []
        if self.left:
            arr.extend(self.left.postorder()) # left subtree
        if self.right:
            arr.extend(self.right.postorder()) # right subtree
        arr.append(self.val) # root
        return arr


def solution(nodeinfo):
    arr = [(i+1, *nodeinfo[i]) for i in range(len(nodeinfo))] # (node number, x, y)
    arr.sort(key=lambda x: (-x[2], x[1])) # sort by y desc x asc
    root = None
    for node in arr:
        node_num, x, y = node
        if root is None:
            root = Node((node_num, x)) # 각 node가 갖는 값은 (node_num, x)

        else:
            root.add((node_num, x))

    preorder = root.preorder()
    postorder = root.postorder()
    return [[val[0] for val in preorder], [val[0] for val in postorder]]


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))