class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        n = len(heights)
        m = len(heights[0]) #SLIGHTLY MODIFIED DJIKSTRA

        start = [0, 0, 0]
        end = [n-1, m-1]

        # 2D grid matrix to track the minimum path efforts found for each coordinate
        efforts = [[float('inf')] * m for k in range(n)]

        efforts[0][0] = 0  
        min_heap = []
        heapq.heappush(min_heap,start)

        dx_dy = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while min_heap:
            last = heapq.heappop(min_heap)
            curr_eff, curr_x, curr_y = last
                                            
            if [curr_x, curr_y] == end:
                return curr_eff
                
            for dx, dy in dx_dy:
                x, y = curr_x + dx, curr_y + dy

                if (x < n) and (x >= 0) and (y < m) and (y >= 0):
                    next_jump = abs(heights[curr_x][curr_y] - heights[x][y])
                    new_eff = max(curr_eff, next_jump)

                    if new_eff < efforts[x][y]:
                        efforts[x][y] = new_eff
                        heapq.heappush(min_heap, [new_eff, x, y])

        return 0


