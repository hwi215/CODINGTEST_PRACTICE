import sys

w, n = map(int, sys.stdin.readline().split())

jew = [list(map(int, input().split())) for _ in range(n)]

jew = sorted(jew, key = lambda x : x[1], reverse = True)

total = 0

for weight, price in jew:
    if w > weight:
        total += weight * price
        w -= weight
    else:
        total += w * price
        break

print(total)