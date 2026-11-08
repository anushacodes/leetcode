class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Count the groups of connected 1s."""
        # dfs in 4 dirs every 1 you find as you iterate through greaph
        # visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # check dirs, change to 0 (visited)
            if r < rows and c < cols and r >= 0 and c >= 0 and grid[r][c] != '0':
                grid[r][c] = '0'
                dfs(r + 1, c) # down
                dfs(r - 1, c) # up
                dfs(r, c + 1) # right
                dfs(r, c - 1) # left
            else:
                return 


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count += 1

        # dfs(rows, cols)

        return count
        