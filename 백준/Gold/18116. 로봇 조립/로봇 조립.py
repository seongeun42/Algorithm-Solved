import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    R = [-1] * (10**6 + 1)
    for _ in range(N):
        cmd = [*input().split()]
        if cmd[0] == 'Q':
            print(-R[find_root(int(cmd[1]), R)])
        elif cmd[0] == 'I':
            a = int(cmd[1])
            b = int(cmd[2])
            ar = find_root(a, R)
            br = find_root(b, R)
            if ar != br:
                if R[ar] < R[br]:
                    R[ar] += R[br]
                    R[br] = ar
                else:
                    R[br] += R[ar]
                    R[ar] = br

solve()