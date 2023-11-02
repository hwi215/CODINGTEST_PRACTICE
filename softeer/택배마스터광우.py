'''
순열 문제 -> 모든 경우의 수에서 최소 값 찾기
'''

import sys
from itertools import permutations

n, m, k = map(int, input().split())
li = list(map(int, input().split()))

li_combi = permutations(li, n)

# check = 1000000
result = sys.maxsize

for i in li_combi:
    answer = 0
    count = 0
    tmp = 0
    i2 = list(i)

    while count != k:
        if count == k:
            break
        target = i2[0]
        while (tmp + target) <= m:
            i2.pop(0)

            tmp += target
            i2.append(target)

            target = i2[0]

        answer += tmp
        count += 1
        tmp = 0
    result = min(result, answer)

# if check > answer:
#     check = answer


print(result)