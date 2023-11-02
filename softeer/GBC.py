'''
[문제]
주어진 구간의 제한속도와 테스트한 구간의 속도를 기준으로
가장 크게 제한 속도를 넘어간 값이 얼마인지 구하는 문제

[문제풀이]
1. 전체 구간 길이가 100으로 한정되어 있으므로 리스트 크기를 100으로 해서 제한 속도 모두 넣기
2. 구간 테스트해서 가장 크게 제한 속도 넘어간 값 갱신
'''

n, m = map(int, input().split())

li = [0 for i in range(101)]

target = 0
for i in range(n):
    a, b = map(int, input().split())
    for j in range(target, target + a):
        li[j] = b
    target += a


#print(li)
target = 0
result = 0

for i in range(m):
    a, b = map(int, input().split())
    for j in range(target, target + a):
        if result < (b - li[j]):
            result = (b-li[j])
    target += a


print(result)
