# 조건문 if
a = 10

if a >= 20:
    print("20이상")
elif a >= 10:
    print("10이상")
else:
    print("10미만")

# 파이썬 기타 연산자
# 1) pass - 아무것도 처리하지 않고 넘어감
score = 80
if score >= 80:
    pass
else:
    print("80점 미만")

print("프로그램 종료")

# 2) 간결하게 작성하기 - 반복문
a = [1, 2, 3, 4, 5]
remove_set = {2, 3}

result = []
for i in a: # 같은표현) [i for i in a if i not in remove_set]
    if i not in remove_set:
        result.append(i)

print(result)

# 3) 간결하게 작성하기 - 부등식
x = 10
if 0 < x < 20: # 같은표현) if x > 0 and x < 20:
    print("x는 0 초과 20 미만의 수 입니다.")