from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = digits.pop()
        carry = (a + 1) // 10
        ans = deque([(a + 1) % 10])
        while digits:
            a = digits.pop()
            ans.appendleft((a + carry)%10)
            carry = (a + carry) // 10
        if carry != 0:
            ans.appendleft(1)
        return list(ans)
