class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0   #Blocked start and endpoint

        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        
        for j in range(m):
            if obstacleGrid[j][0] == 1:
                break
            dp[j][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
