class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        mark = [[False for _ in range(n)] for _ in range(m)]
        for a in range(m):
            for b in range(n):
                if not mark[a][b] and grid[a][b] == "1":
                    count += 1
                    searches = [(a, b)]
                    while searches:
                        i, j = searches.pop()
                        if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == "1" and not mark[i][j]:
                            mark[i][j] = True
                            searches.append((i+1, j))
                            searches.append((i, j+1))
                            searches.append((i-1, j))
                            searches.append((i, j-1))
        return count
