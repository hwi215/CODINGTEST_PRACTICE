n, k = map(int, input().split())

result = 0
while True:
    target = (n//k) * k
    print(target)
    result += (n-target)
    print(result)
    n = target

    if n < k:
        break
    result += 1
    n //= k
result += (n-1)
print("결과")
print(result)