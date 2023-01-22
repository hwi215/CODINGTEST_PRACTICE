# input(): 한 줄 문자열 입력받기
# list(map(int, input().split())): 문자열을 띄어쓰기로 구분하여 각각 정수 자료형 데이터로 저장

# 예시1
n = int(input()) # 데이터 개수 입력 : 5
data = list(map(int, input().split())) # 공백으로 구분해서 입력받기 : 1 2 3 4 5
print(data)

data.sort(reverse = True) # 내림차순
print(data)

# 예시2 - 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())

print(n, m, k)

# 예시3 - 입력갯수가 많은 경우 - sys.stdin.readline()이용
import sys
data = sys.stdin.readline().rstrip() # hello world
print(data) # hello world

a = 1
b = 2
print(a, b) # 1 2 - print는 기본적으로 띄어쓰기
print(a)
print(b)

# 예시4 - 자바와 다르게 파이썬은 수 데이터가 자동으로 문자열로 바뀌지 않는다
answer = 7
print("정답은 " + str(answer) + "입니다.") # 정답은 7입니다.
print("정답은", answer, "입니다.") # 정답은 7 입니다. - 띄어쓰기로 출력됨
print(f"정답은 {answer}입니다.") # 정답은 7입니다. - f-string문법