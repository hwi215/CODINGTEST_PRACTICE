def location(word):
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]

    for i, key in enumerate(keyboard):
        if word in key:
            y = i
            x = key.index(word)
            return x, y

left, right = map(str, input().split())
word = input()

# 모음 저장
consonant = "qwertasdfgzxcv"

answer = 0
for w in word:

    # 현재 그자리
    if w == left or w == right:
        answer += 1

    # x, y 위치 입력받기
    else:
        x_left, y_left = location(left)
        x_right, y_right = location(right)
        # 현재 위치의 x, y 위치
        x, y = location(w)

        if w in consonant: # 모음이면 왼쪽이 이동
            answer += abs(x-x_left) + abs(y-y_left) + 1
            left, x_left, y_left = w, x, y
        else: # 자음이면 오른쪽이 이동
            answer += abs(x-x_right) + abs(y-y_right) + 1
            right, x_right, y_right = w, x, y

print(answer)



