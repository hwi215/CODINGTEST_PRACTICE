n = int(input())
nums = list(map(int, input().split()))

nums.sort()
# 1 2 3 3 4
answer = 0
target = 0
for i in range(n):
    target += nums[i]
    answer += target

print(answer)