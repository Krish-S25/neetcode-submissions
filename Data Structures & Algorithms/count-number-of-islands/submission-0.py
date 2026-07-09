class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(r, c, m, n):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == "0":
                return 

            grid[r][c] = "0" #DESTROY current block 1->0
                             #DESTROY surroundings
            dfs(r-1, c, m, n)  #UP
            dfs(r+1, c, m, n)  #DOWN
            dfs(r, c-1, m, n)  #LEFT
            dfs(r, c+1, m, n)  #RIGHT
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                island_count += 1
                dfs(i, j, m, n)

        return island_count

