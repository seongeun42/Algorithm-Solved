import sys
input = sys.stdin.readline

def recursion(s, e):
    if e - s == 2:
        arr[s], arr[e] = '-', '-'
        return
    cnt = (e - s + 1) // 3
    recursion(s, s + cnt - 1)
    recursion(e - cnt + 1, e)

while 1:
    line = input().rstrip()
    if not line:
        break
    N = int(line)
    if N == 0:
        print('-')
    else:
        arr = [' '] * (3 ** N)
        recursion(0, 3 ** N - 1)
        print(''.join(arr))