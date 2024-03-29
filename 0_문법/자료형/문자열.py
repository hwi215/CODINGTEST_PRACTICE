data = 'Hello'
print(data)

data2 = "Hello"
print(data2)

data3 = "Hello \"hwi\"" # 문자열에 따옴표 쓰기
data4 = "Hello \'hwi\'" # 문자열에 따옴표 쓰기
print(data3)
print(data4)

# 문자열 붙이기
a = 'hello'
b = 'world'
print(a + " " + b)
print(a + b)

# 문자열 곱하기(n번만큼 반복)
print(a * 3)

# 문자열 슬라이싱
a = "abcde"
print(a[0:2])

# 문자열 뒤집기
s = 'hello'
print(s[::-1])

s2 = 'hello'
li = list(s2)
li.reverse() # 리스트로 되어있는 것을 뒤집기
print(li)
print(''.join(li))