# 정수
a = 1000
b = -1000
print(a)
print(b)

# 실수
x = 123.45
y = -123.
z = -.7 # 0생략
print(x)
print(y)
print(z)


# 지수표현
c  = 1e9
d = 12.34e1
e = 12.34e-1
print(c)
print(d)
print(e)

# 파이썬은 실수를 정확히 표현하지 못함
a = 0.3 + 0.6
print(a) # a != 0.9

if a == 0.5:
    print(True)
else:
    print(False)
# 반올림하기, 3째자리에서 반올림
print(round(a, 2))

# 수 연산
a = 7
b = 2

print(a/b) # 나누기
print(a%b) # 나머지
print(a//b) # 몫
print(a**b) # 거듭제곱
