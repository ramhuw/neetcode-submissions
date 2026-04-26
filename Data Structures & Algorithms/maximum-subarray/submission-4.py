class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        m = max(nums)
        while nums and nums[0] < 0:
            nums.remove(nums[0])
        if not nums:
            return m
        l = [0]
        for num in nums:
            l.append(l[-1] + num)
        ma = max(l)
        mi = min(l)
        return ma - mi