n = int(input())

li = [0]
target = 0
answer = []
li2 = []
t = []
for i in range(1, n+1):
    a = int(input())
    t.append(a)
    while li[-1] < a:
        target += 1
        li.append(target)
        answer.append('+')
    if li[-1] == a:
        li2.append(li.pop())
        answer.append('-')

    while li[-1] >= a:
        li2.append(li.pop())
        answer.append('-')

    if li[-1] == a:
        li.append(li[-1])

if t == li2:
    for i in range(len(answer)):
        print(answer[i])
else:
    print('NO')


