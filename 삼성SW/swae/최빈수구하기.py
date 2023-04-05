T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    n = int(input())
    scores = list(map(int, input().split()))
    check = [0 for _ in range(101)]
    for i in scores:
        check[i] += 1

    m = max(check)
    for i in range(len(check) - 1, -1, -1):
        if check[i] == m:
            print("#{} {}".format(n, i))