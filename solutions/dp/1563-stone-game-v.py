class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # Some alpha beta pruning
        dp = {}
        n = len(stoneValue)
        prefix_sum = list(accumulate([0] + stoneValue))

        def stoneGame(left, right):
            if (left, right) in dp:
                return dp[(left, right)]
            
            if left == right:
                return 0
            
            ans = float("-inf")
            for i in range(left, right+1):
                left_sum = prefix_sum[i+1] - prefix_sum[left]
                right_sum = prefix_sum[right+1] - prefix_sum[i+1]
                if left_sum == right_sum:
                    if ans >= 2 * left_sum:
                        continue
                    ans = max(ans, left_sum + max(stoneGame(left, i), stoneGame(i+1, right)))
                elif left_sum > right_sum:
                    if ans >= 2 * right_sum:
                        break
                    ans = max(ans, right_sum + stoneGame(i+1, right))
                else:
                    ans = max(ans, left_sum + stoneGame(left, i))

            dp[(left, right)] = ans
            return dp[(left, right)] 

        return stoneGame(0, n-1)

                 
