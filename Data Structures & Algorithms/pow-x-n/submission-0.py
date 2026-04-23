class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        l = []
        m = []
        k = 0
        while n != 0:
            k += 1
            l.append(n & 1)
            n >>= 1
            if m:
                m.append(m[-1]*m[-1])
            else:
                m.append(x)
        ans = 1
        for i in range(k):
            if l[i]:
                ans *= m[i]
        return ans
        