n = int(input())

for i in range(1, n+1):
    li = list(map(int, str(i)))
    result = int(i) + sum(li)
    if result == n:
        print(i)
        break

    if i == n:
        print(0)
        break

