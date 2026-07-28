import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left and num < - self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        while len(self.left) > len(self.right):
            heapq.heappush(self.right, -heapq.heappop(self.left))
        while len(self.left) + 1 < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))


    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return self.right[0]