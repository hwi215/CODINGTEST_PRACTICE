# 최소신장트리 문제
# 크루스칼 알고리즘
import sys
input = sys.stdin.readline

# find 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드, 간선 수
n, m  = map(int, input().split())


edges = []
# 간선 정보
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()

# 부모 테이블 초기화
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

# 최소 신장 트리 계산 변수 정의
result = []


# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(m):
    cost, a, b = edges[i]
    # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(cost)
        #total_cost += cost

# 두 마을로 분리(가장 큰 비용이 드는 간선 제거)
print(sum(result) - max(result))