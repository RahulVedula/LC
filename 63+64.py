class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if m == 1 or n == 1 or obstacleGrid[0][0] == 1:
            if sum(sum(obstacleGrid,[])) > 0:
                return 0
            return 1
        dp[0][0] = 0
        dp[0][1] = int(obstacleGrid[0][1] == 0)
        dp[1][0] = int(obstacleGrid[1][0] == 0)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 1 and j == 0:
                    continue
                if i == 0 and j == 1:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i > 0 and obstacleGrid[i-1][j] != 1:
                    dp[i][j] += dp[i-1][j]
                if i < m-1 and obstacleGrid[i+1][j] != 1:
                    dp[i][j] += dp[i+1][j]
                if j > 0 and obstacleGrid[i][j-1] != 1:
                    dp[i][j] += dp[i][j-1]
                if j < n-1 and obstacleGrid[i][j+1] != 1:
                    dp[i][j] += dp[i][j+1]
        print(dp)
        return dp[m-1][n-1]
