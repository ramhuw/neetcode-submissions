class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        d = [[(s[i: j] in wordDict) if j >= i else False for j in range(n+1)] for i in range(n)]
        searches = [0]
        searched = set()
        while searches:
            k = searches.pop()
            if k in searched:
                continue
            if k >= n:
                return True
            for j in range(n+1):
                if d[k][j]:
                    searches.append(j)
            searched.add(k)
        return False