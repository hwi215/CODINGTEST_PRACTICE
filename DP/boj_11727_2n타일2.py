import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

dp[1] = 1

if n < 2:
    print(dp[n])
elif n == 2:
    print(3)

else:
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-2] * 2 + dp[i-1]

    print(dp[n] % 10007)