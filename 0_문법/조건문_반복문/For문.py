# 1부터 9까지 모든 값 더하기
result = 0
for i in range(1, 10):
    result += i

print(result)

# 첫 번째 index부터 방문시
scores = [70, 40, 55, 70, 90]
for i in range(5):
    if scores[i] >= 70:
        print(i+1, "번 학생은 합격입니다.")

# 블랙리스트 학생은 제외하고 조건문 적용
scores = [70, 40, 55, 70, 90]
black_list = {1, 2}

for i in range(5):
    if i+1 in black_list:
        continue # 무시 - pass는 첫번째 if문 넘어가고 두번째 if문은 실행함, continue는 첫번째 및 두번재 if문 모두 무시하고 다음 i로 넘어가서 반복문 실행함
    if scores[i] >= 70:
        print(i+1, "번 학생은 합격입니다.")

# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)
