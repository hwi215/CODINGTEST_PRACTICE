n = int(input())

for i in range(n):
    answer = []
    li = list(map(str, input().split()))
    for j in li:
        answer.append(j[::-1])
    print(' '.join(answer))