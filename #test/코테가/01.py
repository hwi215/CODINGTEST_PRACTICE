import heapq
K = 3
user_scores = ["a 100", "b 200", "c 300", "d 50", "a 150", "d 300"]
"""
1 a
2 a b
3 a b c
3 a(150) b(200) c(300)
4 b(200) d(300) c(300)
"""
heap = []
heap2 = []
count = 0
index = 0
answer = 0
t = []
t2 = []
idx = 0
for i in user_scores:
    a, b = i.split()
    print(a, b)

    if len(heap) < K:
        heapq.heappush(heap, (int(b), a))
        answer += 1

    else:
        t = []
        t2 = []
        for x, y in heap:
            t.append(y)

        count = 0
        """
        for i in range(len(heap)-1):
            if heap[i][0] > heap[i+1][0]:
                t.append(heap[i+1][0]) # 작은거 넣기
"""


        if a in t: # 이미 존재
            idx = t.index(a)
            if int(b) > int(heap[idx][0]):
                heapq.heappush(heap, (int(b),a))
            del heap[idx]

        else: # 존재 X
            print(heap[0][0])
            if int(b) > int(heap[0][0]):
                heapq.heappop(heap)
                heapq.heappush(heap, (int(b), a)) # 새로운 값으로 대체
                #answer += 1
            else:
                continue

        for x, y in heap:
            t2.append(y)

        t.sort()
        t2.sort()

        if t != t2:
            answer += 1

        print("t:", t)
        print("t2", t2)

        t = []
        t2 = []

    print(heap, answer)

print(answer)


''' 점수 높은
# elif 먼저 달성
# 새로운 기록 반영
이전보다 낮으면 무시
1페이지는 몇번 바뀌나? 유저 닉네임만 표시
점수 변화가 있어도 랭킹 그대로면 페이지 바뀌지 않음
닉네임 수 = k
유저 닉네임, 점수 달성 순서대로 배열 = user_
'''