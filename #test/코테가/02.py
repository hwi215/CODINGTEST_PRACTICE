
# 3) 중복순열
from itertools import product
lines = [5, 4, 3]
lines.sort(reverse=True)
dots = [1, 5, 8]

result = []
for i in range(1, 4):
    for a in product(lines, repeat=i):
        print(a, len(a))


print(result)
