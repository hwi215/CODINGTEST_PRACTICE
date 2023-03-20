# 목표) 감독관 최소 수 찾기
# 최소 수 -> heap?
import sys

input = sys.stdin.readline
room_num = int(input())

people_nums = list(map(int, input().split()))

b, c = map(int, input().split()) # 총감독관, 부감독관

count = 0 # 감독관 수
for i in range(len(people_nums)):
    if people_nums[i] >= b:
        count += 1
        people_nums[i] -= b
    else: # 총감독관이 감독할 수 있는 학생 수 > room 당 학생수 일 경우 예외처리
        count += 1
        continue

    if people_nums[i]:
        count += people_nums[i] // c # c명씩 부감독관 1명 할당
        if people_nums[i] % c != 0: # c보다 작은 나머지 인원 부감독관 1명 할당
            count += 1

print(count)