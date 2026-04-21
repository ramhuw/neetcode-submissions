class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[board[i][j] for j in range(9)] for i in range(9)]
        columns = [[board[i][j] for i in range(9)] for j in range(9)]
        blocks = [[board[3*a+i][3*b+j] for i in range(3) for j in range(3)] for a in range(3) for b in range(3)]
        return (all([self.isValid(row) for row in rows]) and all([self.isValid(column) for column in columns]) and all([self.isValid(block) for block in blocks]))
    
    def isValid(self, area: List[str]) -> bool:
        map = {}
        for entry in area:
            if entry != ".":
                map[entry] = map.get(entry, 0)
                map[entry] += 1
                if map[entry] > 1:
                    return False
        return True