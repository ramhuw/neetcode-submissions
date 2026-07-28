class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        searches = [(i, j, set()) for i in range(m) for j in range(n)]
        while searches:
            i, j, s = searches.pop()
            s = s.copy()
            l = len(s)
            if l == len(word):
                return True
            if i >= 0 and i < m and j >= 0 and j < n and board[i][j] == word[l] and (i, j) not in s:
                s.add((i, j))
                searches.append((i, j+1, s.copy()))
                searches.append((i+1, j, s.copy()))
                searches.append((i, j-1, s.copy()))
                searches.append((i-1, j, s.copy()))
        return False