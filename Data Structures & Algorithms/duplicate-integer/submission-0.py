class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            v = map.get(num, 0)
            if v > 0:
                return True
            map[num] = 1
        return False