n, k = map(int, input().split())
li = []
for i in range(n):
    li.append(int(input()))

li.sort(reverse=True)

answer = 0
for i in range(n):
    if li[i] <= k:
        answer +=  k // li[i]
        k -= (k // li[i]) * li[i]
print(answer)

