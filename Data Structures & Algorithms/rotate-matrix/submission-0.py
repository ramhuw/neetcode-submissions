class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n % 2 == 0:
            for i in range(n//2):
                for j in range(n//2):
                    (matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i]) = (matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1])
        else:
            for i in range(n//2 + 1):
                for j in range(n//2):
                    (matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i]) = (matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1])
        