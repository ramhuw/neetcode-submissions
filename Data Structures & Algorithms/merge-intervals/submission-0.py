class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        right = len(intervals)
        while left < right:
            middle = (left + right) // 2
            if intervals[middle][0] > newInterval[0]:
                right = middle
            else:
                left = middle + 1
        if left > 0 and intervals[left-1][1] >= newInterval[0]:
            intervals[left-1][1] = max(intervals[left-1][1], newInterval[1])
            left -= 1
        else:
            intervals.insert(left, newInterval)
        while left + 1 < len(intervals) and intervals[left][1] >= intervals[left+1][0]:
            intervals[left][1] = max(intervals[left][1], intervals[left+1][1])
            del intervals[left+1]
            
        return intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for interval in intervals:
            ans = self.insert(ans, interval)
        return ans