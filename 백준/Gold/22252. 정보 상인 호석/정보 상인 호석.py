import sys
input = sys.stdin.readline

def solve():
    Q = int(input())
    gorilla = {}
    hs = 0
    for _ in range(Q):
        query = list(input().rstrip().split())
        if query[0] == '1':
            if query[1] in gorilla:
                gorilla[query[1]].extend([*map(int, query[3:])])
            else:
                gorilla[query[1]] = [*map(int, query[3:])]
        else:
            if query[1] in gorilla:
                info = gorilla[query[1]]
                info.sort()
                for _ in range(int(query[2])):
                    if len(info) == 0:
                        break
                    hs += info.pop()
    print(hs)

solve()