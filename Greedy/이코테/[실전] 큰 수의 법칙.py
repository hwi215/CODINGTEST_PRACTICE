n, m, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort(reverse=True)
target = [nums[0], nums[1]]

sum = 0
count = 0
while True:
    for j in range(k):
        if count == m:
            break
        sum += nums[0]
        count += 1
    if count == m:
        break
    sum += nums[1]
    count += 1


print(sum)


# 5 8 3
# 2 4 5 4 6