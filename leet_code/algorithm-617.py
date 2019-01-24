# https://leetcode.com/problems/merge-two-binary-trees/
'''
접근1: tree를 1d array로 변환한 뒤 비교 => heap이 아니므로 1d array로 변환하기 어려움
접근2: root에서 부터 recursive하게 merge함
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 is None:
            return t2

        if t2 is None:
            return t1

        node = TreeNode(None)
        node.val = t1.val + t2.val
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node