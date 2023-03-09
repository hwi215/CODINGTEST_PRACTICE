n = int(input())
li = []

for i in range(n):
    li.append(input())

li = list(set(li)) # 중복제거
li.sort() # 알파벳 순 정렬

li.sort(key = len) # 길이 순 정렬

for i in li:
    print(i)
"""
li2 = []
for i in range(n):
    s = input()
    l = len(s)
    if s not in li2:
        li.append((l, s))
    li2.append(s)

li.sort(key = lambda  x:x[1])
li.sort(key = lambda x:x[0])

for i, s in li:
    print(s) 
"""