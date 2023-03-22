# 백트래킹으로 풀기 - 시간초과 방지

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxi = -1e9
mini = 1e9

def dfs(count, sum, plus, minus, mul, div):
    global maxi, mini
    if count == n: # 연산자 모두 사용하면 종료
        maxi = max(sum, maxi)
        mini = min(sum, mini)
        return

    # elif가 아닌 각자 모두 if문을 활용하여, 동시에 반복 수행됨
    if plus:
        dfs(count + 1, sum + nums[count], plus-1, minus, mul, div)
    if minus:
        dfs(count + 1, sum - nums[count], plus, minus-1, mul, div)
    if mul:
        dfs(count + 1, sum * nums[count], plus, minus, mul-1, div)
    if div:
        dfs(count + 1, int(sum / nums[count]), plus, minus, mul, div-1)


dfs(1, nums[0], oper[0], oper[1], oper[2], oper[3])
print(maxi)
print(mini)