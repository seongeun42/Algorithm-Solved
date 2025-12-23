import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    group = {}
    member = {}
    for _ in range(N):
        gname = input().rstrip()
        group[gname] = []
        cnt = int(input())
        for _ in range(cnt):
            mname = input().rstrip()
            group[gname].append(mname)
            member[mname] = gname
    for _ in range(M):
        name = input().rstrip()
        if int(input()) == 0:
            print(*sorted(group[name]), sep="\n")
        else:
            print(member[name])

solve()