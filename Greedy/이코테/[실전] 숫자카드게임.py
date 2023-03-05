n, m = map(int, input().split())
nums = []
min_value = 0
result = 0
for i in range(n):
    nums = list(map(int, input().split())) # 한 줄씩 확인
    min_value = min(nums)
    result = max(result, min_value)
print(result)

"""  
li = []
a = 0
for i in range(n):
    nums[i].sort()
    a = nums[i][0] # 제일 작은 숫자
    li.append(a)

li.sort(reverse=True)
print(li[0])
"""
