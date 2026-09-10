class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == 1 and m == 1:
            return grid[0][0]

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        distances = [[float("inf")] * m for _ in range(n)]
        swimming_path = [(grid[0][0], 0, 0)]

        while swimming_path:
            maximum_height, row, col = heapq.heappop(swimming_path)

            if maximum_height > distances[row][col]:
                continue
            
            if row == n-1 and col == m-1:
                return distances[row][col]
            
            for dx, dy in directions:
                newRow, newCol  = row + dx, col + dy
                if 0 <= newRow < n and 0 <= newCol < m and max(grid[newRow][newCol], maximum_height) < distances[newRow][newCol]:
                    distances[newRow][newCol] = max(grid[newRow][newCol], maximum_height) 
                    heapq.heappush(swimming_path, (max(grid[newRow][newCol], maximum_height), newRow, newCol))
        return 0