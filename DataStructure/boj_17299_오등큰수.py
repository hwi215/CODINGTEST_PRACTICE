import sys
from collections import Counter
from collections import deque
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

c = Counter(nums)
answer = [-1] * n
stack = deque()
for i in range(len(nums)):
    while stack and (c[stack[-1][0]] < c[nums[i]]):
        a, index = stack.pop()
        answer[index] = nums[i]
    stack.append([nums[i], i])

print(*answer)

