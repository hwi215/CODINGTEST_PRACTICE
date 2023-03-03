n = int(input())

li = [0 for i in range(10)]
check = [False for i in range(10)]
count = 0

for i in range(n):
    a, b = map(int, input().split())
    if check[a-1] == False:
        check[a - 1] = True
        li[a-1] = b
    else:
        if li[a-1] != b:
            count += 1
            li[a-1] = b

print(count)

