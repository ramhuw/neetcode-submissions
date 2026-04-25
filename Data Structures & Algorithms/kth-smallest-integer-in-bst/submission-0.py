# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        search = [(root, False, False)]
        counter = 0
        while search:
            (node, lflag, rflag) = search.pop()
            if not lflag:
                search.append((node, True, False))
                if node.left:
                    search.append((node.left, False, False))
            elif not rflag:
                if node.right:
                    search.append((node.right, False, False))
                
                search.append((node, True, True))
            else:
                counter += 1
                if counter == k:
                    return node.val