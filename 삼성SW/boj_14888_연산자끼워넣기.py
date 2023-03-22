# 목표) 연산값의 최댓값 / 최솟값 찾기
# 브루트포스?
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

li = []
oper2 = []

for i in range(4):
    if oper[i] > 0:
        for j in range(oper[i]):
            oper2.append(i)

#print(oper2)

# oper2로 조합
result2 = list(permutations(oper2, len(oper2))) # 3개 뽑는 모든 순열 구하기
#print(result2)

min = 1e9
max = -1e9

for c in permutations(oper2, n - 1):
    result = nums[0]
    for i in range(1, n):
        a = nums[i]
        if c[i-1] == 0:
            result += a
        elif c[i-1] == 1:
            result -= a
        elif c[i-1] == 2:
            result *= a
        elif c[i-1] == 3:
            result = int(result / a)

    if result > max:
        max = result
    if result < min:
        min = result

print(max)
print(min)



