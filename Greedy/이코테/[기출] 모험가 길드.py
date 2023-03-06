n = int(input())
levels = list(map(int, input().split()))

# 1 2 2 2 3
levels.sort()
i = 0

count = 0
people = 0
for level in levels:
    people += 1
    if level <= people:
        count += 1
        people = 0


print(count)


