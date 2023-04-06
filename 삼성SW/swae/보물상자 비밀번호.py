T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, k = map(int, input().split())
    s = input()
    li = list(s)
    result = []
    t = ''
    count = 0
    for i in range(n // 4):
        for j in range(n):
            t += li[j]
            count += 1
            if count == n // 4:
                result.append(t)
                t = ''
                count = 0
        a = li.pop()
        li.insert(0, a)

    result = list(set(result))
    result.sort(reverse=True)

    print("#{} {}".format(test_case, int(result[k - 1], 16)))