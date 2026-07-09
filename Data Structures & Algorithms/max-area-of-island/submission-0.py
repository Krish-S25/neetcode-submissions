class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):

            # OUT OF BOUNDS OR WATER
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
            # DESTROY CURRENT LAND
            grid[r][c] = 0

            # CURRENT CELL + ALL 4 DIRECTIONS
            return ( 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1)   + dfs(r, c + 1) )

        max_area = 0

        # SCAN ENTIRE GRID
        for i in range(m):
            for j in range(n):

                # SKIP WATER
                if grid[i][j] == 0:
                    continue

                # FIND AREA OF CURRENT ISLAND
                current_area = dfs(i, j)

                # UPDATE ANSWER
                max_area = max(max_area, current_area)

        return max_area