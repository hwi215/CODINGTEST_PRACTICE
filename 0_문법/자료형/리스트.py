a = [1, 2, 3]
print(a)

# 인덱스 0의 값
print(a[0])

# 빈 리스트 선언
x = list()
y = []
print(x) # []
print(y) # []

# 크기가 n이고, 모든 값이 0인 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5]
print([-1]) # 뒤에서 첫번째 원소
print([-3]) # 뒤에서 세번째 원소
a[3] = 77 # 원소 값 변경
print(a[0:4]) # 0번째 원소부터 (4-1)번째 원소까지

# 리스트 컴프리핸션(1차원)
arr = [i for i in range(10) if i % 2 == 0] # 0부터 19까지 수 중에서 짝수만 포함하는 리스트
print(arr)

arr2 = [i*i for i in range(1, 10)] # 1부터 9까지 수의 제곱 값을 포함하는 리스트
print(arr2)

# 리스트 컴프리핸션(2차원)
n = 3
m = 4
arr = [[1] * m for _ in range(n)] # [0] * 열 for _ in range(행)
print(arr)

# 리스트 관련 기타 메소드
# 1) append() - 값 삽입
a = [1, 2, 3]
print(a)
a.append(4) # 리스트에 값 삽입
print(a)

# 2) sort()
a.sort() # 오름차순 정렬
a.sort(reverse = True) # 내림차순 정렬
print(a)

# 3) reverse() - 리스트 원소 뒤집기
a.reverse()
print(a)

# 4) insert() - 특정 인덱스에 값 추가 / O(n) 느림
a.insert(0, 9)
print(a)

# 5) remove(1) - 특정값 1 삭제(1이 여러개 있어도 하나만 삭제함) / O(n) 느림
a.insert(0, 1)
print(a)
a.remove(1)
print(a)

# remove로 제거하는 것보다 빠른 방법
a = [1, 2, 3, 4, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set] # remove_set에 없는 값만 저장
print(result)


