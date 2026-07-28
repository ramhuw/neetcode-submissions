class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)
        for i in range(0, n):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(ans):
                ans = s[left+1: right]
            left = i - 1
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(ans):
                ans = s[left+1: right]
        return ans