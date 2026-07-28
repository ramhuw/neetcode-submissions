class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    d[i+1][j+1] = 1 + d[i][j]
                else:
                    d[i+1][j+1] = max(d[i][j+1], d[i+1][j])
        return d[n][m]