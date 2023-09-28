import heapq

n = int(input())
li = []
for _ in range(n):
    start, end = map(int, input().split())
    li.append((start, end))

li = sorted(li, key = lambda x : (x[0], x[1]))

room = []
heapq.heappush(room, li[0][1]) # 끝나는 시간 넣기
print(room)

count = 0
for i in range(1, n):
    if li[i][0] < room[0]: # 다음 수업 시작 시간 < 현재 수업 끝나는 시간
        count += 1
        heapq.heappush(room, li[i][1]) # 끝나는 시간 추가

    else:
        heapq.heappop(li)
        heapq.heappop(room, li[i][1]) # 끝나는 시간 추가


print(len(room))


