s = input()
alpa = []
sum = 0
for i in s:
    if i.isalpha(): # 알파벳인지 확인
        alpa.append(i)
    else:
        sum += int(i)

alpa.sort()

if sum != 0:
    alpa.append(str(sum))

print(''.join(alpa))

# K1KA5CB7