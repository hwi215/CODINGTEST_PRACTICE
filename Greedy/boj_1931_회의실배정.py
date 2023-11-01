n = int(input())

li = []
for _ in range(n):
    start, end = map(int, input().split())
    li.append((start, end))

# 빨리 끝나는 순, 빨리 시작하는 순으로 정렬
li = sorted(li, key = lambda x : (x[1], x[0]))

start = 0
end = 0
count = 0
for a, b in li:
    if end <= a: # 종료된 시점 <= 새로운 강의 시작시간
        start = a
        end = b
        count += 1

print(count)
