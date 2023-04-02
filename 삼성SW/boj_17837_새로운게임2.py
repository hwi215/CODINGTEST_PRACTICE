n, k = map(int, input().split())
chess = [[[] for _ in range(n)] for _ in range(n)]
piece = []
board = [list(map(int, input().split())) for _ in range(n)] # 흰 빨 파

for i in range(k):
    r, c, d = map(int, input().split())
    piece.append([r-1, c-1, d-1]) # r, c, d (0부터)
    chess[r-1][c-1].append(i) # 체스 번호 저장

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

count = 0


def game(num):
    r, c, d = piece[num]
    nr = r + dr[d]
    nc = c + dc[d]
    # 범위 벗어남 or 파란색
    if 0 > nr or nr >= n or 0 > nc or nc >= n or board[nr][nc] == 2:
        # a번 말의 이동방향 반대로 하고 한 칸 이동
        if d in [0, 2]:
            d += 1
        elif d in [1, 3]:
            d -= 1

        piece[num][2] = d
        nr = r + dr[d]
        nc = c + dc[d]
        # 방향 바꾸고 또 범위 벗어남 or 방향바꿈이면? 그대로
        if 0 > nr or nr >= n or 0 > nc or nc >= n or board[nr][nc] == 2:
            return True

    piece_up = []
    for index, piece_num in enumerate(chess[r][c]):
        if piece_num == index:
            piece_up.extend(chess[r][c][index:])
            chess[r][c] = chess[r][c][:index]
            break

    # 빨간색 인 경우
    if board[nr][nc] == 1:
        piece_up = piece_up[-1::-1] # 뒤집기

    for h in piece_up:
        piece[h][0], piece[h][1] = nr, nc
        chess[nr][nc].append(h)

    if len(chess[nr][nc]) >= 4:
        return False

    return True

while True:
    check = False
    if count > 1000:
        print(-1)
        break
    for i in range(k):
        if game(i) == False:
            check = True
            break
    count += 1
    if check:
        print(count)
        break





