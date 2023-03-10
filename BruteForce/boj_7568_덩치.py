n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

answer = []
for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        else:
            fir_a, fir_b = li[i][0], li[i][1]
            sec_a, sec_b = li[j][0], li[j][1]
            if fir_a < sec_a and fir_b < sec_b:
                count += 1

    answer.append(count+1)

print(*answer)

