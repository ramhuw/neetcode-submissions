class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        w = [0 for _ in range(0, n)]
        wo = [0 for _ in range(0, n)]
        for i in range(0, n):
            wo[i] += nums[i]
            if i > 0:
                w[i] += max(w[i-1], wo[i-1])
                wo[i] += w[i-1]
        return max(wo[n-1], w[n-1])