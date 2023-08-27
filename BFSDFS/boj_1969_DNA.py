# 1969 DNA

n, len = map(int, input().split())
li = []
for i in range(n):
    li.append(input())

# A C G T
str = ["A", "C", "G", "T"]
count = [[0]*4 for _ in range(len)]

for i in range(n):
    target = li[i]
    for j in range(len):
        if target[j] == "A":
            count[j][0] += 1
        elif target[j] == "C":
            count[j][1] += 1
        elif target[j] == "G":
            count[j][2] += 1
        elif target[j] == "T":
            count[j][3] += 1

answer = "" # Hamming Distance합이 가장 작은 DNA
answer_sum = 0 # Hamming Distance

for i in range(len):
    max_value = 0;
    # A C G T 각각 최대값에 해당하는 알파벳, 인덱스 찾기
    for j in range(4):
        if count[i][j] > max_value:
            max_value = count[i][j]
            maxIdx = j
    answer += str[maxIdx]
    answer_sum += sum(count[i]) - max(count[i]) # Hamming Distance값 계산

print(answer)
print(answer_sum)





