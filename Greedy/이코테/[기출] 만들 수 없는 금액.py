n = int(input())
coins = list(map(int, input().split()))

# 1 1 2 3 9
coins.sort()

target = 1
for i in coins:
    if target < i:
        break
    target += i

print(target)