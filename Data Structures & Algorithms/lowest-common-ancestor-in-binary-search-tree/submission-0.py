# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ppath = self.searchPath(root, p)
        qpath = self.searchPath(root, q)
        ans = None
        while ppath and qpath:
            a = ppath.pop()
            b = qpath.pop()
            if a == b:
                ans = a
            else:
                break
        return ans
    def searchPath(self, root: TreeNode, p: TreeNode) -> List[TreeNode]:
        stack = [(root, False)]
        ppath = []
        back = None
        found = False
        while stack:
            current = stack.pop()
            if current[0] is None:
                continue
            elif current[1]:
                if found and (current[0].left == back or current[0].right == back):
                    ppath.append(current[0])
                    back = current[0]
                continue
            elif not current[1] and not found:
                if current[0].val == p.val:
                    found = True
                    back = current[0]
                    ppath.append(current[0])
                    continue
                stack.append((current[0], True))
                stack.append((current[0].left, False))
                stack.append((current[0].right, False))
        return ppath