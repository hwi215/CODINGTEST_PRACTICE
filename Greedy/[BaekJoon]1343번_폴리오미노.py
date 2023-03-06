n = input()
n = n.replace("XXXX", "AAAA") # 냅다 바꾸기
n = n.replace("XX", "BB")

print(n)
if 'X' in n:
    print(-1)
else:
    print(n)