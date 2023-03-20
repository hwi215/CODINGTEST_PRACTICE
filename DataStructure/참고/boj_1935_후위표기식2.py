from collections import deque
n = int(input())
s = input()
l = []
stack = deque()
for i in range(n):
    l.append(int(input()))


answer = l[0]
for i in s:
    if i.isalpha():
        stack.append(l[ord(i) - ord('A')])
    else:
        s2 = stack.pop()
        s1 = stack.pop()

        if i == '*':
            stack.append(s1 * s2)
        elif i == '+':
            stack.append(s1 + s2)
        elif i == '/':
            stack.append(s1 / s2)
        elif i == '-':
            stack.append(s1 - s2)

print('%.2f' %stack[0])


