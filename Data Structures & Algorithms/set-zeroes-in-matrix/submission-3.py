class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        cdic = set()
        rdic = set()
        for i in range(m):
            flag = False
            for j in range(n):
                if matrix[i][j] == 0 and j not in cdic:
                    cdic.add(j)
                    flag = True
                    for u in range(m):
                        if matrix[u][j] == 0:
                            rdic.add(u)
                        matrix[u][j] = 0
            if flag or i in rdic:
                matrix[i] = [0] * n
            
                
                

