class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1]
        suffix_prod = [1]
        for i in range(1, n):
            prefix_prod.append(prefix_prod[i-1]*nums[i-1])
            suffix_prod.append(suffix_prod[i-1]*nums[n-i])
        return [prefix_prod[i]*suffix_prod[n-1-i] for i in range(n)]
