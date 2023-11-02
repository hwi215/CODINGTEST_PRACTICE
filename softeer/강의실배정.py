import heapq

'''
[문제]
김교수는 강의실 1개에 최대한 많은 강의를 배정하려고 한다. 
배정된 강의는 서로 겹치지 않아야 하며 수업시간의 길이와 상관없이 최대한 강의를 많이 배정하라. 
단, 두 강의의 시작시간과 종료시간은 겹쳐도 된다.

[문제풀이]
sort, lambda 정렬은 시간초과 남
-> heapq 우선순위 큐 사용하기!(앞에 있는 것 기준으로 적은것부터 자동 정렬됨)  
'''
n = int(input())

li = []
for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(li, (b, a))  # 빨리 끝나는 순으로 정렬하기 위해

now = 0
answer = 0

while li:
    b, a = heapq.heappop(li)
    if now <= a:  # 예약 가능한 시작 시간 <= 강의 시작시간
        answer += 1
        now = b  # 예약 가능한 시작 시간 = 강의 끝나는 시간으로 갱신

print(answer)