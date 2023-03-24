import sys
from collections import deque

input = sys.stdin.readline

# 톱니 상태 저장 - rotate 사용하기 위해 deque로 바꿔서 저장
li = [deque(list(map(int,input().rstrip()))) for _ in range(4)]

k = int(input())

for _ in range(k):
    check = [] # 각 톰니의 2번째, 6번째 톱니 값만 따로 저장(비교할 값)
    num, d = map(int, input().split())
    for i in range(4):
        check.append([li[i][6], li[i][2]])
    num -= 1 # 톱니 0부터 시작

    # 비교
    # 1) 왼쪽 톱니랑 비교
    if num != 0:
        for j in range(num, 0, -1): # 4번째 톱니부터 2번째 톱니까지 (왼쪽 톱니가 존재한느 톱니들)
            if check[j][0] != check[j-1][1]: # 톱니 값 다르면
                if (num - (j - 1)) % 2 == 0:
                    li[j - 1].rotate(d)
                elif (num - (j - 1)) % 2 != 0:
                    li[j - 1].rotate(-1 * d)
            else:
                break

    # 2) 오른쪽 톱니랑 비교
    if num != 3:
        for j in range(num, 3):
            if check[j][1] != check[j+1][0]:
                if (num - (j + 1)) % 2 == 0:
                    li[j + 1].rotate(d)
                elif (num - (j + 1)) % 2 != 0:
                    li[j + 1].rotate(-1 * d)
            else:
                break

    li[num].rotate(d)


score = [1, 2, 4, 8]
sum = 0
for i in range(len(li)):
    if li[i][0] == 1:
        sum += int(score[i])

print(sum)




