class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ps = set()
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            ps.add((i, 0))
        for j in range(n):
            ps.add((0, j))
        pg = [[False for j in range(n)] for i in range(m)]
        while ps:
            i, j = ps.pop()
            if pg[i][j]:
                continue
            pg[i][j] = True
            if i > 0 and heights[i-1][j] >= heights[i][j]:
                ps.add((i-1, j))
            if i < m - 1 and heights[i+1][j] >= heights[i][j]:
                ps.add((i+1, j))
            if j > 0 and heights[i][j-1] >= heights[i][j]:
                ps.add((i, j-1))
            if j < n - 1 and heights[i][j+1] >= heights[i][j]:
                ps.add((i, j+1))
        at = set()
        for i in range(m):
            at.add((i, n-1))
        for j in range(n):
            at.add((m-1, j))
        ag = [[False for j in range(n)] for i in range(m)]
        while at:
            i, j = at.pop()
            if ag[i][j]:
                continue
            ag[i][j] = True
            if i > 0 and heights[i-1][j] >= heights[i][j]:
                at.add((i-1, j))
            if i < m - 1 and heights[i+1][j] >= heights[i][j]:
                at.add((i+1, j))
            if j > 0 and heights[i][j-1] >= heights[i][j]:
                at.add((i, j-1))
            if j < n - 1 and heights[i][j+1] >= heights[i][j]:
                at.add((i, j+1))
        ans = []
        for i in range(m):
            for j in range(n):
                if pg[i][j] and ag[i][j]:
                    ans.append([i, j])
        return ans