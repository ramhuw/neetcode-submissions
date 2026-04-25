class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(2**n):
            subset = []
            for j in range(n):
                if (i >> j) & 1:
                    subset.append(nums[j])
            ans.append(subset)
        return ans