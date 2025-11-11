import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = input().rstrip()
        center = 5 * (10 ** (len(N)-1)) - 1
        if int(N) >= center:
            print(center * (center + 1))
            continue
        else:
            num_1 = int(N)
            num_2 = ''
            for i in N:
                num_2 += str(9 -int(i))
            num_2 = int(num_2)
            print(num_1 * num_2)
            continue

solve()