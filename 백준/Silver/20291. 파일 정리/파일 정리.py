import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    file = sorted([input().rstrip().split('.')[1] for _ in range(N)])
    cnt = 1
    for i in range(1, len(file)):
        if file[i - 1] == file[i]:
            cnt += 1
        else:
            print(file[i - 1], cnt)
            cnt = 1
    print(file[-1], cnt)

solve()