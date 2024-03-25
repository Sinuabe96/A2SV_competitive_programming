class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
          n = len(grid)
          maxLocal = []
        
          for i in range(n - 2): 
            row = []
            for j in range(n - 2):

                max_val = grid[i][j]

                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        max_val = max(max_val, grid[x][y])
                row.append(max_val)
            maxLocal.append(row)
        
          return maxLocal
