class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = 0
        counter = 0
        hel = 0
        ans = 0
        for n in nums:
            if n > m:
                m = n
            ans ^= counter
            hel ^= n
            counter += 1
        ans ^= counter
        return ans ^ hel
        
            
