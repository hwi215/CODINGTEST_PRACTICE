# 문자열 비교 - 하나만 틀린 문자열이면 True, 아니면 False
# 6/7 통과
def solution(param0):
    answer = True
    check = 0
    for i in range(len(param0)):
        for j in range(i+1, len(param0)):
            count = 0
            s1 = param0[i]
            s2 = param0[j]
            #print(s1, s2)
            for t in range(len(s1)):
                if str(s1[t]) == str(s2[t]):
                    #print(s1[t], s2[t])
                    count += 1

        if count == len(param0[0])-1:
            check += 1
        else:
            check += 0

        #print(check)
        if check > 0:
            answer = True
        else:
            answer = False



    return answer