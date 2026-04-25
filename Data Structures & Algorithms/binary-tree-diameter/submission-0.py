# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _ = self.depth(root)
        return self.diameter
    def depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return -1
        left = node.left
        right = node.right
        ld = self.depth(left) + 1
        rd = self.depth(right) + 1
        self.diameter = max(self.diameter, ld + rd)
        return max(ld, rd)