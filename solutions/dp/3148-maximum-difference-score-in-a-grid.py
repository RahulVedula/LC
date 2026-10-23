class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        dp = {}
        n, m = len(grid), len(grid[0])
        def getMaxScore(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            right = down = float("-inf")
            if 0 <= i < n and 0 <= j + 1 < m:
                right = grid[i][j+1] - grid[i][j] + max(0, getMaxScore(i, j+1))
            
            if 0 <= i+1 < n and 0 <= j < m:
                down = grid[i+1][j] - grid[i][j] + max(0, getMaxScore(i+1, j))

            dp[(i, j)] = max(float("-inf"), right, down)
            return dp[(i, j)]

        getMaxScore(0, 0)
        return max(dp.values()) if max(dp.values()) != float("-inf") else -1
 