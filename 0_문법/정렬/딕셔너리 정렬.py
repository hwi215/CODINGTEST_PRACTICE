dic = {'pop': 3100, 'classic': 1450, 'trot':620}

# key 값을 기준으로 오름차순 정렬하여 리스트 출력
print(sorted(dic))
# key 값을 기준으로 내림차순 정렬한 리스트 출력
print(sorted(dic, reverse=True))

# key 값을 기준으로 정렬된 (key,value) 원소쌍을 가진 리스트 출력
print(sorted(dic.items()))

# key 값을 기준을 정렬된 딕셔너리 생성
dic = dict(sorted(dic.items()))
print(dic)


# value 값을 기준으로 오름차순 정렬하여 (k, v) 리스트 반환
print(sorted(dic.items(), key=lambda x:x[1]))
# 위 값을 딕셔너리로 변환
print(dict(sorted(dic.items(), key=lambda x:x[1])))
# value 값을 기준으로 오름차순 정렬
print(sorted(dic,key=lambda x:dic[x]))

# dic.items()의 경우 (key, value) 튜플 형태의 원소를 제공하기에 lambda에서 x[1]와 같은 방식으로 value 값을 지정할 수 있는 것이다.