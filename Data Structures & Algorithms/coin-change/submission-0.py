class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        l = [-1] * (amount + 1)
        l[0] = 0
        coins = list(filter(lambda x: x <= amount, coins))
        coins.sort()
        for coin in coins:
            for i in range(amount + 1):
                if l[i] != -1:
                    counter = 1
                    while i + counter * coin <= amount:
                        step = l[i] + counter
                        if l[i + counter * coin] == -1 or l[i + counter * coin] > step:
                            l[i + counter * coin] = step
                        counter += 1
        return l[-1]
