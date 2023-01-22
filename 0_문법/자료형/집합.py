# set: 중복허용X, 순서X

# 집합 자료형 초기화 방법1 - set()함수 이용
data = set([1, 2, 3, 4, 1, 2])
print(data)

# 집합 자료형 초기화 방법2 - {}이용
data = {1, 2, 3, 1, 2, 2}
print(data)

# 집합 자료형 연산
a = set([1, 2, 3])
b = set([3, 4, 5])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

# 1) 값 추가 - add
data.add(4)
print(data)

# 2) 여러 값 추가 - update
data.update([5, 6])
print(data)

# 3) 특정한 값을 갖는 원소 삭제 - remove
data.remove(3)
print(data)