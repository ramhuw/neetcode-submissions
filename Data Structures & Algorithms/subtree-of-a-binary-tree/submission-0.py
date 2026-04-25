# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        current = self.isSameTree(root, subRoot)
        if root is not None:
            current = current or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return current
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        elif p is None and q is None:
            return True
        else :
            return p.val == q.val and (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)) 
    