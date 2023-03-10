n = int(input())

num = 0
count = 0
c = 0 # 0번째
while True:
    num += 1
    c += 1
    if '666' in str(num):
        count += 1

    if count == n:
        print(num)
        break