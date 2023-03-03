# permutations: 순열 = nCr => 순서고려
# combinations: 조합 = nPr => 순서고려 X
# product: 중복허용 순열
# combinations_with_replacement: 중복허용 조합

# 1) 순열
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 3개 뽑는 모든 순열 구하기
print(result)

# 2) 조합
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 3개 뽑는 모든 순열 구하기
print(result)

# 3) 중복순열
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개 뽑는 중복순열 구하기
print(result)

# 4) 중복조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2)) # 2개 뽑는 중복조합 구하기
print(result)
