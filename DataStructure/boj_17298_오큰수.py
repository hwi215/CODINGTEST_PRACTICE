import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

answer = [-1] * n
stack = deque()

for i in range(n):
    while stack and (stack[-1][0] < nums[i]):
        a, index = stack.pop()
        answer[index] = nums[i]
    stack.append([nums[i], i])

print(*answer)


