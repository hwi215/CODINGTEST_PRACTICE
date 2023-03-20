import sys

input = sys.stdin.readline # 시간초과 문제 해결
n = int(input())
st = []
def fun_push(st, x):
    st.append(x)

def fun_pop(st):
    if len(st) == 0:
        print(-1)
    else:
        a = st.pop()
        print(a)

def fun_size(st):
    print(len(st))

def fun_empty(st):
    if len(st) == 0:
        print(1)
    else:
        print(0)

def fun_top(st):
    if len(st) == 0:
        print(-1)
    else:
        print(st[-1])

li = []
for i in range(n):
    li = list(map(str, input().split()))
    fun = li[0]
    if fun == 'push':
        x = li[1]
        fun_push(st, x)
    elif fun == 'pop':
        fun_pop(st)
    elif fun == 'size':
        fun_size(st)
    elif fun == 'empty':
        fun_empty(st)
    elif fun == 'top':
        fun_top(st)
