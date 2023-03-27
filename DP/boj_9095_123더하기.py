def dp123(n):
    dp = [0 for _ in range(n+1)]
    if n < 3:
        return n
    elif n == 3:
        return 4
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]

c = int(input())

for i in range(c):
    n = int(input())
    print(dp123(n))




