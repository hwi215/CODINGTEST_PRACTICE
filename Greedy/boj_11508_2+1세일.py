n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

answer = 0
target = 0
if len(li) < 3:
    for i in li:
        answer += i
else:
    li.sort(reverse=True)
    for i in range(1, n+1):
        if i % 3 != 0:
            answer += li[i-1]

print(answer)

# 6 5 5 5 5 4
# 11 10