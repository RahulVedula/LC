class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * (days[-1]+1)
        dp[0] = 0
        for i in range(1, days[-1]+1):
            if i in days:
                option1 = costs[0] + dp[max(0, i-1)]
                option2 = costs[1] + dp[max(0, i-7)]
                option3 = costs[2] + dp[max(0, i-30)]
                #print(option1, option2, option3, i)
                dp[i] = min(option1, option2, option3)
            else:
                dp[i] = dp[i-1]
        return dp[-1]

        
