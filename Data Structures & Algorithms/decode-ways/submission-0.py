class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        ans = [0 for _ in range(len(s) + 1)]
        ans[0] = 1
        for i in range(1, len(s) + 1):
            if s[i-1] != "0":
                ans[i] += ans[i-1]
            if i > 1 and ((int(s[i-2]) == 2 and int(s[i-1]) <= 6) or int(s[i-2]) == 1):
                ans[i] += ans[i-2]
        return ans[len(s)]