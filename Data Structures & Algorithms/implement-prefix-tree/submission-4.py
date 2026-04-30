class PrefixTree:

    def __init__(self):
        self.heads = []

    def insert(self, word: str) -> None:
        current = self.heads
        for c in word:
            flag = True
            for node in current:
                if node and node.val == c:
                    flag = False
                    current = node.children
                    break
            if flag:
                newNode = Node(c)
                current.append(newNode)
                current = newNode.children
        current.append(None)
            
            

    def search(self, word: str) -> bool:
        current = self.heads
        for c in word:
            flag = True
            for node in current:
                if node and node.val == c:
                    flag = False
                    current = node.children
                    break
            if flag:
                return False
        if None in current:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        current = self.heads
        for c in prefix:
            flag = True
            for node in current:
                if node and node.val == c:
                    flag = False
                    current = node.children
                    break
            if flag:
                return False
        return True
class Node:

    def __init__(self, val):
        self.val = val
        self.children = []
    def add(self, child):
        self.children.append(child)