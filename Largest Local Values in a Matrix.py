class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = []
    
        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                submatrix = [
                grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                grid[i][j - 1], grid[i][j], grid[i][j + 1],
                grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
                ]
           
                max_value = max(submatrix)
                row.append(max_value)
            max_local.append(row)
    
        return max_local
