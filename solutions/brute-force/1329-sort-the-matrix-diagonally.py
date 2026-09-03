class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        current_index = 0

        for i in range(n-1, -1, -1):
            x, y = i, 0
            nums = []
            while 0 <= x < n and 0 <= y < m:
                nums.append(mat[x][y])
                x += 1
                y += 1

            nums.sort()
            x, y = i, 0
            for num in nums:
                mat[x][y] = num
                x += 1
                y += 1

        
        for j in range(1, m):
            x, y = 0, j
            nums = []
            while 0 <= x < n and 0 <= y < m:
                nums.append(mat[x][y])
                x += 1
                y += 1

            nums.sort()
            x, y = 0, j
            for num in nums:
                mat[x][y] = num
                x += 1
                y += 1
        
        return mat
        
