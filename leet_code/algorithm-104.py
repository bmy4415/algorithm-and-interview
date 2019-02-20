# https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
tree 관련 문제는 recursion으로 해결되는 경우가 많음
current node부터 leaf node까지의 높이 = 1 + (좌우 subtree의 높이 중 큰 것)
임을 이용
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)