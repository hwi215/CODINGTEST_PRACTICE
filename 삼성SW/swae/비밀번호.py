for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, s = input().split()
    n = int(n)
    li = list(s)

    i = 0
    while True:
        if li[i] == li[i+1]:
            li = li[:i] + li[i+2:]
            n -= 2
            i -= 2
        i += 1
        if i == n-1:
            break
    s = ''
    s = ''.join(li)
    print("#{} {}".format(test_case, s))