class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0]*n
        for i in range(n):
            while len(stack) > 0:
                if temperatures[stack[-1]] < temperatures[i]:
                    poped_index = stack.pop()
                    ans[poped_index] = i - poped_index
                else:
                    break
            stack.append(i)
        return ans




        