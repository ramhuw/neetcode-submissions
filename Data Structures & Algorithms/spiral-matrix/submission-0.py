class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        mn = m * n
        (i, j) = (0, 0)
        counter = 0
        ans = []
        while counter != mn:
            for v in range(j, n - j):
                counter += 1
                ans.append(matrix[i][v])
            for u in range(i + 1, m - i):
                counter += 1
                ans.append(matrix[u][n - j - 1])
            if counter == mn:
                break
            for v in reversed(range(j, n - j - 1)):
                counter += 1
                ans.append(matrix[m - 1 - i][v])
            if counter == mn:
                break
            for u in reversed(range(i + 1, m - i - 1)):
                counter += 1
                ans.append(matrix[u][j])
            i += 1
            j += 1

        return ans
