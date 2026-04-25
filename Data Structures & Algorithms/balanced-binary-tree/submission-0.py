# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _ = self.depth(root)
        return self.balanced
    def depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        left = root.left
        right = root.right
        ld = self.depth(left) + 1
        if self.balanced is False:
            return 0
        rd = self.depth(right) + 1
        if self.balanced is False:
            return 0
        if ld > rd + 1 or ld < rd - 1:
            self.balanced = False
            return 0
        return max(ld, rd)
