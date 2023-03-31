# 미팅 ?
# 8 / 10 통과
import heapq
from collections import Counter

def solution(n, meetings):
    heap = []
    li = []
    times = []
    result = 0 

    for i in meetings:
        start, end = i[0], i[1]
        time = int(end) - int(start) + int(start)
        times.append(time)

    for i in range(len(times)):
        if len(heap) < n:
            heapq.heappush(heap, [times[i], i])
        else:
            t, index = heapq.heappop(heap)
            li.append(index)
            heapq.heappush(heap, [t + times[i], index])

    while len(heap) != 0:
        t, index = heapq.heappop(heap)
        li.append(index)

    answer = Counter(li)

    k = []
    for i in list(answer):
        k.append([i, answer[i]])
    #print(k)
    for i in range(len(k)-1):
        if k[i][1] == k[i+1][1]:
            if k[i][0] < k[i+1][0]:
                result = k[i][0]
            else:
                result = k[i+1][0]

        else:
            result = k[i][0]
            break


    return result