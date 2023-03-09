# (키, 값)
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

print(data) # {'사과': 'Apple', '바나나': 'Banana'}

# 존재여부 확인
if '사과' in data:
    print("사과 존재")

# 사전 자료형 관련 함수
# 1) key 데이터만 담은 리스트
key_list = data.keys()
print(key_list)

# 2) value 데이터만 담은 리스트
value_list = data.values()
print(value_list)

# 3) 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])
