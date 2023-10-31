s = input()
max_count = 0
heap_max = []
s = s.upper()
li = [0] * 26

for i in s:
    tmp = ord(i) - 65
    li[tmp] += 1

max_num = max(li)

count = 0
for i in range(len(li)):
    if li[i] == max_num:
        target = i + 65
        count += 1

if count == 1:
    print(chr(target))
else:
    print("?")




