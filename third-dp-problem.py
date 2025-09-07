def frog_jump(ind, height, dp):
    if(ind == 0 ):
        return 0
    if dp[ind]!= -1 :
        return dp[ind]
    left = frog_jump(ind-1, height, dp) + abs(height[ind]- height[ind-1])
    right = float('inf')
    if ind>1:
        right = frog_jump(ind-2, height, dp) + abs(height[ind] - height[ind-2])
    dp[ind] = min(left, right)
    return dp[ind]
height=[10,60,40,30,20]
n = len(height)
dp = [-1] *(n+1)
print(frog_jump(n-1,height,dp))