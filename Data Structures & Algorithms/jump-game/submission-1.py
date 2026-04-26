class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        b = [False] * n
        b[0] = True
        for i in range(n - 1):
            if b[i]:
                for j in range(nums[i]+1):
                    if i + j < n:
                        if i + j == n - 1:
                            return True
                        b[i + j] = True
        return b[-1]