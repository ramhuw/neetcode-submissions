class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[[]]]
        for i in range(1, target + 1):
            dpi = []
            for num in nums:
                if num <= i:
                    for s in dp[i - num]:
                        dpi.append(s + [num])
            dp.append(dpi)
        ans = set()
        for d in dp[target]:
            d.sort()
            ans.add(tuple(d))
        return [list(a) for a in ans]

