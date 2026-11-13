class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cnt = 0

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "0":
                grid[r][c] = "0"
                dfs(r + 1, c)
                dfs(r -1 , c)
                dfs(r, c+1)
                dfs(r, c-1)
            else:
                return

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    cnt += 1

        return cnt


            

        