# 목표) 최대 수익 구하기
# dp
n = int(input())
li = []
dp = [0] * (n+1) # 맨 마지막 값도 동일한 로직을 적용하기 위해서 n+1 크기로 초기화

for _ in range(n):
    t, p = map(int, input().split())
    li.append([t, p])

# 뒤에서 부터
for i in range(n-1, -1, -1): # n-1부터 0까지
    if i + li[i][0] > n: # n일을 넘어갈 경우
        dp[i] = dp[i+1] # 이전 값으로 설정
    else:
        # 오늘 상담 안할경우([이전 이익])와 상담 할 경우([li[i][0]일 후 이익 + (i+1)일의 이익] 중 큰 값으로 설정)
        dp[i] = max(dp[i+1], dp[i + li[i][0]] + li[i][1])

    #print(dp)

print(dp[0])




