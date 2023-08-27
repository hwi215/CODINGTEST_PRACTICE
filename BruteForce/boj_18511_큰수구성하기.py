# 18511 큰 수 구성하기

from itertools import product

n, k = map(int, input().split())
li = list(map(int, input().split()))

# 내림차순 정렬
li = sorted(li, reverse = True)

answer = ""

len = len(str(n)) # 문자 자리 수
check = False
while check == False: # 찾을 때가지 반복
    prod = list(product(li, repeat= len)) # 중복순열
    for i in prod:
        tmp = ""
        for j in i:
            tmp += str(j)

        if(int(tmp) <= n): # 찾았다
            print(tmp)
            check = True
            break

    if check == False: # 처음 문자 자리수에서 찾는 숫자가 없으면 자리수 다운하기
        len -= 1











