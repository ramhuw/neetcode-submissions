class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        counter = 0
        current = self.head
        while counter != index:
            if current.next is None:
                return -1
            current = current.next
            counter += 1
        if current is None:
            return -1
        return current.val
        

    def insertHead(self, val: int) -> None:
        new_head = Node(val, self.head)
        self.head = new_head
        

    def insertTail(self, val: int) -> None:
        tail = Node(val, None)
        if self.head is None:
            self.head = tail
            return None
        current = self.head
        while current.next != None:
            current = current.next
        current.next = tail

    def remove(self, index: int) -> bool:
        if index == 0 and self.head != None:
            self.head = self.head.next
            return True
        current = self.head
        counter = 0
        while counter < index - 1:
            if current is None:
                return False
            current = current.next
            counter += 1
        if current != None and current.next != None:
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        ans = []
        current = self.head
        while current != None:
            ans.append(current.val)
            current = current.next
        return ans

class Node:

    def __init__(self, val, node):
        self.val = val
        self.next = node

        
