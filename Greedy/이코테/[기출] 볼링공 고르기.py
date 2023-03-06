n, m = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i+1, n):
        if nums[i] != nums[j]:
            count += 1

print(count)
