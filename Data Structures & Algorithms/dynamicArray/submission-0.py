class DynamicArray:
    
    def __init__(self, capacity: int):
        self.data = [None] * capacity
        self.ready = 0

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n
        if self.ready <= i:
            self.ready = i + 1

    def pushback(self, n: int) -> None:
        if self.ready >= self.getCapacity():
            self.resize()
        self.data[self.ready] = n
        self.ready += 1

    def popback(self) -> int:
        self.ready -= 1
        r = self.data[self.ready]
        self.data[self.ready] = None
        return r

    def resize(self) -> None:
        self.data += [None] * self.getCapacity()

    def getSize(self) -> int:
        return len([x for x in self.data if x is not None])
    
    def getCapacity(self) -> int:
        return len(self.data)
