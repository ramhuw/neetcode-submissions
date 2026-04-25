# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.mx(root.left) < root.val and self.mi(root.right) > root.val and self.isValidBST(root.left) and self.isValidBST(root.right)

    def mx(self, root):
        if root is None:
            return -1001
        else:
            return max([root.val, self.mx(root.left), self.mx(root.right)])
    def mi(self, root):
        if root is None:
            return 1001
        else:
            return min([root.val, self.mi(root.left), self.mi(root.right)])