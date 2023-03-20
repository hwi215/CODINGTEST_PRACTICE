n = int(input())


for i in range(n):
    s = input()
    answer = []
    for j in s:
        if j == '(':
            answer.append(j)
        else:
            if len(answer) != 0:
                if answer[-1] == '(':
                    answer.pop()
            else:
                answer.append(j)

    if len(answer) != 0:
        print('NO')
    else:
        print('YES')
