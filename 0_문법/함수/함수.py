# 함수 만들기1
def add(a, b):
    return a+b

print(add(2, 3))

# 함수 만들기2
def add2(a, b):
    print("a+b:", a+b)

add2(2, 3)

# global로 변수 선언
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 람다식 이용
def add3(a, b):
    return a + b

print((lambda a, b: a+b)(2, 3)) # 같은표현) print(add(2, 3))