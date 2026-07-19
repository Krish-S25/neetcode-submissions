class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #MODIFIED DJIKSTRA
        n = len(grid)
        visited = [[False]*n for _ in range(n)]

        minHeap = [(grid[0][0], 0, 0)]

        visited[0][0] = True
        dx_dy = [(-1,0), (1,0), (0,1), (0,-1)]

        while minHeap :
            min_val, x, y = heapq.heappop(minHeap)

            if x == n-1 and y == n-1:
                return min_val
            
            for dx, dy in dx_dy:
                newX = x + dx
                newY = y + dy
                if newX in range(n) and newY in range(n) and visited[newX][newY]==False:
                    visited[newX][newY] = True
                    bottleneck = max(min_val , grid[newX][newY])

                    heapq.heappush(minHeap, (bottleneck, newX, newY) )
                
        return 0



        