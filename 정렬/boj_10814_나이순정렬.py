n = int(input())
li = []
for i in range(n):
    age, name = map(str, input().split())
    li.append((int(age), name))

li.sort(key = lambda x:x[0])

for i in li:
    print(i[0], i[1])