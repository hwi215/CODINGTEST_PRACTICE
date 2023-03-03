s = input()

word = ['q', 'u', 'a', 'c', 'k']
visited = [False] * len(s)

idx = 0
cnt = 0
if len(s) % 5 != 0:
    print(-1)
    exit()
else:
    for a in range(len(s)):
        if s[a] == 'q' and not visited[a]:
            first = True
            for i in range(len(s)):
                if word[idx] == s[i] and not visited[i]:
                    visited[i] = True
                    if s[i] == 'k':
                        if first:
                            cnt += 1
                            first = False
                        idx = 0
                        continue
                    idx += 1

if cnt == 0 or not all(visited):
    print(-1)
else:
    print(cnt)

