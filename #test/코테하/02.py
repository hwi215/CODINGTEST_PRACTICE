# 새로운 스케줄 [3, 10]에 따라 기존 스케줄 변경하는 문제
# 2/7 통과

def solution(schedules, newSchedule):
    answer = []
    li = []
    for i in range(len(schedules)):
        start, end = schedules[i][0], schedules[i][1]
        if end <= newSchedule[0]:
            continue
        else:
            if start <= newSchedule[0] and end <= newSchedule[1]:
                schedules[i][0] = start
                schedules[i][1] = newSchedule[1]

    for i in schedules:
        answer.append(i)

    return answer

