n = input()

target = len(n) / 2

sum_left = 0
sum_right = 0
for i in range(len(n)):
    if i < target:
        sum_left += int(n[i])
    else:
        sum_right += int(n[i])

if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")