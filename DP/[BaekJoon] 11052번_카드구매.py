# 개미 전사와 같은 문제
'''
n = int(input())
# 비용
cost = list(map(int, input().split()))
cost.insert(0,0)
dp = [0 for _ in range(n+1)]

# DP
# 재귀

for i in range(1, n+1): # 1부터 n까지
    # f(4)를 구한다면, f(1), f(2), f(3) 중에서 최대 값 찾기
    # 반복
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + cost[k])
        #print(dp[i])

print(dp[n])

'''
n = int(input())
li = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + li[k])

print(dp[n])
