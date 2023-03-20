import sys
input = sys.stdin.readline
s = input()
ss = list(sys.stdin.readline().rstrip())
print(ss)
n = int(input())


ss2 = []
for i in range(n):
    fun = list(map(str, input().split()))
    f = fun[0]
    if f == 'P':
        num = fun[1]
        ss.append(num)
    elif f == 'L':
        if ss:
            ss2.append(ss.pop())

    elif f == 'D':
        if ss2:
            ss.append(ss2.pop())
    elif f == 'B':
        if ss:
            ss.pop()

ss.extend(reversed(ss2))
print(''.join(ss))



