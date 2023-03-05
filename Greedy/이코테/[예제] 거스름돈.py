n = int(input())

coins = [500, 100, 50, 10]

count = 0
for coin in coins:
    if int(n // coin) > 0:
        count += int(n // coin) # 몫으로 계산하기
        n = n - int(n // coin) * coin # n %= coin (나머지로 계산하기)

print(count)

