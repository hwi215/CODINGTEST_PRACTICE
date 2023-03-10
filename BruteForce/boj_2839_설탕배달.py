n = int(input())

# 5 3

count = 0
t = 0
while True:
    t += 1
    if n % 5 == 0:
        count += n//5
        print(count)
        break
    else:
        n -= 3
        count += 1
    if n == 0:
        print(count)
        break

    if t > n:
        print(-1)
        break