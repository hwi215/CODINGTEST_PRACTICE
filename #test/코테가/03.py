# 커피머신 문제
import heapq # 최소힙 사용
# [3, 2, 2, 5, 4]
N = 3
coffee_times = [3, 2, 2, 5, 4]

heap = []
li = []
for i in range(len(coffee_times)):
    if len(heap) < N:
        heapq.heappush(heap, (coffee_times[i], i+1))
    else:
        min, index = heapq.heappop(heap)
        print(min, index)
        li.append(index) # 결과 값에 넣기
        heapq.heappush(heap, (min + coffee_times[i], i+1))


while (len(heap) != 0):
    min, index = heapq.heappop(heap)
    li.append(index)

print(li)

'''
answer = []
    stack = []
    #stack = [[1, coffee_times[0]], [2, coffee_times[1]], [3, coffee_times[2]]]
    i = 1
    count = 0
    li = []
    while len(li) < len(coffee_times):
        if i < len(coffee_times)-1:
            stack.append([i+1, coffee_times[i]])
            i += 1
        elif len(stack) == N:
            stack.sort(key = lambda x:x[1])

            for a,b in stack:
                li.append(a)
                stack.pop()
        li =  [2, 3, 1, 5, 4]
        '''

