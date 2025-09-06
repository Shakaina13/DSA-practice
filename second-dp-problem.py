class Solution:
    def climbStairs(self, n):
        dp = [-1]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[i]
    
sol = Solution()
print(sol.climbStairs(3))
