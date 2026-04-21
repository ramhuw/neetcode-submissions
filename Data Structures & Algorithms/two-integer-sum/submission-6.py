class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ori = nums[:]
        nums.sort()
        l = 0
        r = len(nums) - 1
        while True:
            if nums[l] + nums[r] == target:
                break
            while nums[l] + nums[r] < target:
                l += 1
            while nums[l] + nums[r] > target:
                r -= 1
        a = None
        b = None
        for i in range(len(ori)):
            if (ori[i] == nums[l] or ori[i] == nums[r]) and a is None:
                a = i
                continue
            if a is not None and ori[i] + ori[a] == target:
                b = i
        return [a, b]