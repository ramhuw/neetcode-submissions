class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(0, n):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
            left = i - 1
            right = i + 1
            ans += 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
        return ans