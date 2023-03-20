s = input()

li = []
count = 0
for i in range(len(s)):
    if s[i] == "(":
        li.append(s[i])
    else:
        if s[i-1] == "(":
            li.pop()
            count += len(li)
        else:
            li.pop()
            count += 1


print(count)