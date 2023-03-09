array = [[50, "apple"], [30, "banana"] , [400, "melon"]]

# key를 기준으로 오름차순 정렬
array.sort(key = lambda x:x[0])
print(array)

# value를 기준으로 오름차순 정렬
array.sort(key = lambda x:x[1])
print(array)

# key가 여러개 일때 - 다중조건 정렬
array2 = [("A", 18, 300000) , ("F", 24, 10000), ("T", 24, 200000),("Q",24,5000000), ("B", 70, 5000)]
# (<이름> , <나이> , <재산>) 이라고 하면

# 나이를 기준으로 오름차순 정렬하고, 같은 나이라면 재산을 내림차순으로 정렬
array2.sort(key = lambda x: (x[1], -x[2]))
print(array2)