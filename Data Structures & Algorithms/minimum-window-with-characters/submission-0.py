class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = dict()
        for c in t:
            target[c] = target.get(c, 0) + 1
        left = 0
        right = 0
        work = dict()
        ans = None
        while True:
            flag = True
            for k, v in target.items():
                if v > work.get(k, 0):
                    flag = False
                    break
            if flag:
                if ans is None or len(s[left: right]) < len(ans):
                    ans = s[left: right]
                work[s[left]] = work.get(s[left], 0) - 1
                left += 1
            else:
                if right == len(s):
                    break
                work[s[right]] = work.get(s[right], 0) + 1
                right += 1
        return "" if ans is None else ans