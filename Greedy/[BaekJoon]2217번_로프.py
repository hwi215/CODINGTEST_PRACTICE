n = int(input()) #로프 개수
a = []

for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True) #내림차순
result = []
for i in range(n):
    result.append(a[i] * (i+1)) 

print(max(result))