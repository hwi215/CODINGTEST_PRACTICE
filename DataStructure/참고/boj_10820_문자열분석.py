import sys
input = sys.stdin.readline
while True:
    line = input().rstrip('\n')
    if not line:
        break
    l, u, d, s = 0, 0, 0, 0
    for target in line:
        if target.islower(): # 소문자
            l += 1
        elif target.isupper(): # 대문자
            u += 1
        elif target.isdigit(): # 숫자
            d += 1
        elif target.isspace(): # 공백
            s += 1

    print(l, u, d, s)