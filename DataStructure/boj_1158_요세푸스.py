import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

q = deque()
li = []
for i in range(1, n+1):
    q.append(i)

i = 1
while q:
    if i % k == 0:
        li.append(str(q.popleft()))
    else:
        a = q.popleft()
        q.append(str(a))
    i += 1



print("<%s>" %(", ".join(li)))