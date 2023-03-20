s = input()
answer = [-1] * 26
for i in range(len(s)):
    a = ord(s[i]) - ord('a')
    if answer[a] == -1:
        answer[a] = i

print(*answer)

