import sys
s = list(input())
print(s)
# 오른쪽 공백 삭제해서 입력받아 list
ss = list(sys.stdin.readline().rstrip())
print(ss)