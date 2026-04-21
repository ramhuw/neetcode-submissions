class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        ans = 0
        for price in prices:
            ans = max(price - m, ans)
            m = min(m, price)
        return ans
        