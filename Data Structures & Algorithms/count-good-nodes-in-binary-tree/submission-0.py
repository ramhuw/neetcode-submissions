# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return len(self.getNodes(root))
    def getNodes(self, root: Optional[TreeNode]) -> list[TreeNode]:
        if root is None:
            return []
        else:
            l = self.getNodes(root.left)
            r = self.getNodes(root.right)
            return [root] + list(filter(lambda x: x.val >= root.val, l)) + list(filter(lambda x: x.val >= root.val, r))