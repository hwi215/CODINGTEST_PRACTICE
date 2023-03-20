s1 = []
s2 = []

# extend 스택 이어붙이기
# reversed(s2) 스택s2 뒤집
s1.extend(reversed(s2))

li = [1,2,3]
# 삽입
li.append(5)
# 삭제
li.pop()

# 마지막 요소
a = li[-1]

li = [1]
# 비어있는 지 확인
if len(li) == 0:
    print("비어있음")
else:
    print("비어있지 않음")

if li: # 비어있지 않음
    print("not empty")