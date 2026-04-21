class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = set()
        al = set(nums)
        longest = 0
        for num in al:
            if num - 1 not in al:
                start.add(num)
        for num in start:
            i = 0
            while num + i in al:
                i += 1
            longest = max(longest, i)
        return longest
        