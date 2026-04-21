class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while True:
                if nums[i] + nums[j] + nums[k] == 0 and j != k:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                if j >= k:
                    break
                while nums[i] + nums[j] + nums[k] < 0 and j < k:
                    j += 1
                while nums[i] + nums[j] + nums[k] > 0 and j < k:
                    k -= 1
            
        return [list(op) for op in ans]