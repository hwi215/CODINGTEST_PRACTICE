import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    com = list(map(str, input().split()))
    fun = com[0]
    if fun == 'push':
        q.append(com[1])
    elif fun == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif fun == 'size':
        print(len(q))
    elif fun == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif fun == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif fun == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)


