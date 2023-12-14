class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        rows = len(mat)
        columns = len(mat[0])
        for i in range(rows):
            for j in range(columns):
                if(mat[i][j] == 1):
                    sumValueOfRows = sum(mat[i])
                    sumValueOfColumns = sum(mat[row][j] for row in range(rows))
                    if sumValueOfRows == 1 and sumValueOfColumns == 1:
                        count = count + 1
                else:
                    pass
        return count
