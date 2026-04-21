class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        m = {}
        ans = 0
        counter = 0
        i = 0
        while 0 <= i < n:
            if s[i] in m:
                i = m[s[i]] + 1
                ans = max(ans, counter)
                counter = 0
                m = {}
            m[s[i]] = i
            counter += 1
            i += 1
        return max(ans, counter)