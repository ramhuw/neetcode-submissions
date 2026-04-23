class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        u = 0
        d = m - 1
        mid = None
        while u + 1 < d:
            mid = (u + d) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                u = mid
            else:
                d = mid
        row = u if target < matrix[d][0] else d
        l = 0
        r = n - 1
        mid = None
        while l + 1 < r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid
            else:
                r = mid
        return any([matrix[row][column] == target for column in [l, r]])
        
        
            