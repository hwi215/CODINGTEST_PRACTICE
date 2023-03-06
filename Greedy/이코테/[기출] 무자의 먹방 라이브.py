def solution(food_times, k):
    answer = 0
    count = 0
    target = 0
    a = 0
    """  
    c = k // len(food_times)
    na = k % len(food_times)

    for i in range(len(food_times)):
        b = food_times[i]
        b -= c
        food_times[i] = b

    if na == 0:
        for i in range(len(food_times)):
            if food_times[i] != 0:
                target = i
                break 

    else:
        k = na
    """

    while True:
        zeor_count = 0
        if count == k + 1:
            target = i + 1
            break
        if zeor_count == len(food_times):
            target = -1
            break

        for i in range(len(food_times)):
            if food_times[i] != 0:
                a = food_times[i]
                a -= 1
                food_times[i] = a
                count += 1
            else:
                zeor_count += 1

            if count == k + 1:
                target = i + 1
                break
            if zeor_count == len(food_times):
                target = -1
                break

    return target