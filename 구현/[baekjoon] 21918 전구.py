num, n = map(int, input().split())
li = list(map(int, input().split()))

for i in range(n):
    a, b, c = map(int, input().split())
    if a == 1:
        li[b-1] = c
    elif a == 2:
        for j in range(b-1, c):
            if li[j] == 0:
                li[j] = 1
            else:
                li[j] = 0
    elif a == 3:
        for j in range(b-1, c):
            li[j] = 0
    elif a == 4:
        for j in range(b-1, c):
            li[j] = 1

print(*li)


