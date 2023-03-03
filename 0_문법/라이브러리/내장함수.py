# input(), print()
# sum(), max(), min()
# eval(), sorted(), sort()

# sum()
result = sum([1, 2, 3])
print(result)

# max(), min()
li = [1, 2, 3]
result2 = max(li)
result3 = min(1, 2, 3) # min(li)도 가능
print(result2)
print(result3)

# eval() - 수식이 문자열로 들어오면 수식을 계산한 결과값을 반환함
result = eval("(3+5) * 7")
print(result)

# sorted() - iterable객체가 들어왔을 때, 정렬된 결과 반환함
iter = sorted([1, 3, 2, 4]) # 오름차순
print(iter)
iter = sorted([1, 3, 2, 4], reverse = True) # 내림차순
print(iter)

# 튜플 일 경우 특정 기준에 따라 정렬하기 - value값으로 정렬(lambda이용)
tup = sorted([('김아무개', 10), ('박아무개', 5), ('최아무개', 25)], key = lambda x : x[1], reverse = True)
tup2 = sorted([('김아무개', 10), ('박아무개', 5), ('최아무개', 25)], key = lambda x : x[1])
print(tup)
print(tup2)

# 튜플아니면 그냥 sort()도 가능
li = [2, 1, 8, 3]
li.sort() # 오름차순
print(li)
li.sort(reverse = True) # 내림차순
print(li)



