n = int(input())

answer = 0
result = 0
li = []
for _ in range(n):
    li.append(int(input()))

li.sort(reverse=True)

for i in range(n):
    answer = li[i] - (i)
    if answer > 0:
        result += answer

print(result)