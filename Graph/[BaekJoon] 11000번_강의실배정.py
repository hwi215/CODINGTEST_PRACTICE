import sys, heapq
'''
1. 현재 회의실에서 회의가 끝나는 시간 > 다음 회의의 시작 시간
   : 회의실 하나 개설(+1)
2. 현재 회의실에서 회의가 끝나는 시간 < 다음 회의의 시작 시간
   : 현재 존재하는 회의실에서 그대로 진행
'''
input = sys.stdin.readline # 시간초과 해결
n = int(input())
li = []
for _ in range(n):
    start, end = map(int, input().split())
    li.append((start, end))

li = sorted(li, key = lambda x : (x[0], x[1]))

room = []
heapq.heappush(room, li[0][1]) # 첫 회의 종료 시간

count = 1
for i in range(1, n): # 두번째 회의부터
    if room[0] > li[i][0]: # 현재 회의실에서 회의가 끝나는 시간 > 다음 회의의 시작 시간
        count += 1
        heapq.heappush(room, li[i][1]) # 끝나는 시간 추가

    else: # 현재 회의실에서 이어서 진행
        heapq.heappop(room) # 끝나는 시간 갱신을 위해 pop
        heapq.heappush(room, li[i][1]) # 끝나는 시간 추가

#print(len(room))
print(count)


