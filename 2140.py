class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]
        for i in range(len(questions)-2, -1, -1):
            option2 = float("-inf")
            option1 = max(questions[i][0], questions[i+1][0])
            if questions[i][1] + i + 1 < len(questions):
                print(questions[i], i)
                option2 = questions[i][0] + dp[questions[i][1] + i + 1]
            dp[i] = max(option1, option2, dp[i+1])
        print(dp)
        return max(dp)
        
