import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0
while i < len(word):
    if word[i] == "<":
        i += 1
        while word[i] != ">":
            i += 1
        i += 1
    elif word[i].isalnum(): # 숫자나, 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        t = word[start:i]
        t.reverse()
        word[start:i] = t
    else:
        i += 1
print(''.join(word))
