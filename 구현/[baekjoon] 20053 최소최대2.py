import sys

n = int(input())
for i in range(n):
    num = int(input())
    li = list(map(int, input().split()))
    mi = min(li)
    mx = max(li)
    print(str(mi), str(mx))

