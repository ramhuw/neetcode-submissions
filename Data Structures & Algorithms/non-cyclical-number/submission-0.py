class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while True:
            if n == 1:
                return True
            if n in d:
                return False
            d.add(n)
            m = 0
            while n != 0:
                m += (n % 10)**2
                n //= 10
            n = m
