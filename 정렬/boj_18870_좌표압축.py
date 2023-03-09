n = int(input())
li = list(map(int, input().split()))
li2 = list(set(li))
dic = dict()

li2.sort()
for i in range(len(li2)):
    dic[li2[i]] = i


for a in li:
    print(dic[a], end = ' ')


