s = input()

answer = [0] * 26

for i in s:
    a = ord(i) - ord('a')
    answer[a] += 1

print(*answer)