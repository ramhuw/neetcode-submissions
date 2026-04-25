# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            ans = [[root.val]]
            l = self.levelOrder(root.left)
            r = self.levelOrder(root.right)
            while l or r:
                level = []
                if l:
                    level += l.pop(0)
                if r:
                    level += r.pop(0)
                ans.append(level)
            return ans