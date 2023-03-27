n = int(input())

# 가로 1로 1개 or 가로 2로 2개
dp = [0] * (n+1)

if n <= 3:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n] % 10007)