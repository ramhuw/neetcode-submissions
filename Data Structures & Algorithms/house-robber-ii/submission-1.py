class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        w = [0 for _ in range(0, n)]
        wo = [0 for _ in range(0, n)]
        for i in range(0, n):
            if i > 0:
                w[i] = max(w[i-1], wo[i-1])
            if i < n - 1:
                wo[i] = nums[i]
                if i > 0:
                    wo[i] += w[i-1]
        ans1 = w[n-1]
        w = [0 for _ in range(0, n)]
        wo = [0 for _ in range(0, n)]
        for i in range(0, n):
            if i < n - 1 and i > 0:
                w[i] = max(w[i-1], wo[i-1])
            if i > 0:
                wo[i] = nums[i] + w[i-1]
        ans2 = wo[n-1]
        return max(ans1, ans2)