class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = []
        rowsNumber = len(grid)
        columnsNumber = len(grid[0])
        countForRows = 0
        countForColumns = 0
        rows = []
        columns = []
        # lets now find out the number of ones in each row
        for i in range(rowsNumber):
            for j in range(columnsNumber):
                if grid[i][j] == 1:
                    countForRows = countForRows + 1
            rows.append(countForRows)
            countForRows = 0

        # lets now find out the number of ones in each column
        for j in range(columnsNumber):
            for i in range(rowsNumber):
                if grid[i][j] == 1:
                    countForColumns = countForColumns + 1
            columns.append(countForColumns)
            countForColumns = 0


        for i in range(rowsNumber):
            for j in range(columnsNumber):
                grid[i][j] = rows[i] + columns[j] - (rowsNumber-rows[i]) - (columnsNumber-columns[j])

        return grid 
