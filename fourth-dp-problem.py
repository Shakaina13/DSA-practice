def frog_jump(n, k , height):
    dp = [-1]* n

    def solve(i):
        if i == 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        
        min_cost = float('inf')
        for j in range(1, k+1):
            if i-j>=0:
                cost = solve(i-j) + abs(height[i] - height[i-j])
                min_cost = min(min_cost, cost)
        dp[i] = min_cost
        return dp[i]
    return solve(n-1)
height = [30, 10, 60, 10, 60, 50]
n = 6
k =3
print(frog_jump(n , k, height))