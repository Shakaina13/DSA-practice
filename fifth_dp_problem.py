def max_sum(dp, height, ind):
    if ind == 0:
        return height[ind]
    if ind<0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    pick = height[ind] + max_sum(dp, height, ind -2)
    not_pick = 0 + max_sum(dp, height, ind -1)

    dp[ind] = max(pick, not_pick)
    return dp[ind]

height = [2,1,4,9]
n = len(height)
dp = [-1] * n
print(max_sum(dp, height, n-1))