s = input()


result = 0
answer = 0
for i in range(len(s)):
    if i == 0:
        a, b = s[i], s[i+1]
    elif i != 1:
        a, b = result, s[i]
    result = max(int(a)*int(b), int(a)+int(b))
    answer = result

print(answer)
