"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    m = dict()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is not None:
            if self.m.get(node) is None:
                new_node = Node(node.val)
                self.m[node] = new_node
                new_node.neighbors = list(map(self.cloneGraph, node.neighbors))
                return new_node
            else:
                return self.m.get(node)
        else:
            return None