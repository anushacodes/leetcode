class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # from (sc,sr) find all valid right,left,up,down cells and color
        rows = len(image) 
        cols = len(image[0])

        org = image[sr][sc]
        
        def dfs(r, c):
            # starting from sr, sc, check all dirs and keep coloring 
            # (dfs from each new grid)
            if not (0 <= r < rows and 0 <= c < cols):
                return 

            if image[r][c] != org:
                return 
            
            if org == color:
                return

            image[r][c] = color

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + dr, c + dc)

        dfs(sr, sc)

        return image
                    








