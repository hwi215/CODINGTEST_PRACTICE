# 주어진 이진수s에 1~n까지 이진수로 변환한 숫자가 모두 들어있는 지 확인
# 10/10 모두 통과

def solution(s, n):
    answer = True
    num = 0
    for i in range(1, n+1):
        num = format(i, 'b')
        if num not in s:
            answer = False
            break


    return answer
