import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(set([*map(int, input().split())]))
        M = int(input())
        B = list(set([*map(int, input().split())]))
        K = int(input())
        C = list(set([*map(int, input().split())]))
        lucky = set()
        for a in A:
            for b in B:
                for c in C:
                    e = a + b + c
                    tmp = set(list(str(a + b + c)))
                    if len(tmp - {'5', '8'}) == 0:
                        lucky.add(e)
        print(len(lucky))

solve()