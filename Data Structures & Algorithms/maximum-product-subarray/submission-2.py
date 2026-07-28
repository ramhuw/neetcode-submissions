class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mi = None
        ma = None
        ans = None
        for i in range(len(nums)):
            mat = None
            mit = None
            if nums[i] < 0:
                if mi is None:
                    mit = nums[i]
                else:
                    mat = mi * nums[i]
                    mit = nums[i]
                if ma is not None:
                    mit = ma * nums[i] if mit is None else min(mit, ma * nums[i])
                
            if nums[i] > 0:
                if ma is None:
                    mat = nums[i]
                else:
                    mat = ma * nums[i]
                if mi is not None:
                    mit = mi * nums[i]
            
            if nums[i] == 0:
                mat = None
                mit = None
            ma = mat 
            mi = mit 
            if ans is None:
                ans = nums[i]
            ans = max(ans, nums[i])
            if ma is not None:
                ans = max(ma, ans)
        return ans