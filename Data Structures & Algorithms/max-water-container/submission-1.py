class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        ans = 0
        while l < r:
            while heights[l] < heights[r] and l < r:
                ans = max(ans, heights[l] * (r - l))
                l += 1
            while heights[l] > heights[r] and l < r:
                ans = max(ans, heights[r] * (r - l))
                r -= 1
            while heights[l] == heights[r] and l < r:
                ans = max(ans, heights[r] * (r - l))
                for i in range(l+1, r):
                    ans = max(ans, min(heights[i], heights[r]) * max(i - l, r - i))
                l += 1
                r -= 1
        return ans