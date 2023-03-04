current_location = input()

row = int(current_location[1])
col = int(ord(current_location[0])) - int(ord('a')) + 1 # 1로 시작

locations = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

count = 0
for location in locations:
    next_row = row + int(location[0])
    next_col = col + int(location[1])
    if next_row < 1 or next_row > 8 or next_col < 1 or next_col > 8:
        continue
 
    count += 1

print(count)