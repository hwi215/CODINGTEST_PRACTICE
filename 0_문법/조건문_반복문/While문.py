x = 1
result = 0

# 1부터 9까지 더하기
while x < 10:
    result += x
    x += 1

print(result)

# 1부터 9까지 수 중에서 홀수만 더하기
x2 = 0
result2 = 0
while x2 < 10:
    if x2 % 2 == 1:
        result2 += x2
    x2 += 1

print(result2)

