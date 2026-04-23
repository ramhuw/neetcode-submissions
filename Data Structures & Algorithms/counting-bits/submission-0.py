class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            j = i
            a = 0
            while j != 0:
                if 1 & j:
                    a += 1
                j = j >> 1
            ans.append(a)
        return ans