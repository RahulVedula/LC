class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:
        dp = {}
        size_1, size_2 = len(cost), len(cost[0])

        def connectGraphs(i, visited):
            if visited in dp:
                return dp[visited]

            if visited == (1 << (size_1 + size_2)) - 1:
                return 0

            curr_bit = 1 << i
            min_cost = float("inf")
            if curr_bit & visited:
                connectGraphs(i+1, visited)
            
            if i < size_1:
                for j in range(size_2):
                    next_visited = visited | curr_bit
                    next_visited |= (1 << size_1 + j)
                    min_cost = min(min_cost, cost[i][j] + connectGraphs(i+1, next_visited))
            else:
                k = i - size_1
                for j in range(size_1):
                    next_visited = visited | curr_bit
                    min_cost = min(min_cost, cost[j][k] + connectGraphs(i+1, next_visited))

            dp[visited] = min_cost
            return min_cost
        
        return connectGraphs(0, 0)
            
