def fib(n, dp):
    if n<=1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-2,dp) + fib(n-1,dp)
    return dp[n]
n = 3
dp = [-1]* (n+1)
res = fib(n,dp)
print(res)
