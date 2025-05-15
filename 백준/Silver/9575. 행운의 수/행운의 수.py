import sys
input = sys.stdin.readline

def is_lucky(num):
    while num > 0:
        if num % 10 not in {5, 8}:
            return False
        num //= 10
    return True

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = [*map(int, input().split())]
        M = int(input())
        B = [*map(int, input().split())]
        K = int(input())
        C = [*map(int, input().split())]
        lucky = set([a + b + c for c in C for b in B for a in A if is_lucky(a + b + c)])
        print(len(lucky))

solve()