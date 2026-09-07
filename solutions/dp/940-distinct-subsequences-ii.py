class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = {}
        n = len(s)
        MOD = 10**9+7

        def distinct(i):
            if i in dp:
                return dp[i]

            if i >= n:
                return 1
            
            take = 2 * distinct(i+1)
            for j in range(i+1, n):
                if s[j] == s[i]:
                    take -= distinct(j+1)
                    break
            dp[i] = take 
            return dp[i]
        
        distinct(0)
        return (distinct(0) - 1) % MOD

        