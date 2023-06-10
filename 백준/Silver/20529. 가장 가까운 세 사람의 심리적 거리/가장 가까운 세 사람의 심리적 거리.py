import sys
input = sys.stdin.readline

def cal(m1, m2):
    s = 0
    for i in range(4):
        if m1[i] != m2[i]:
            s += 1
    return s

def select():
    ans = 12
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                v = cal(M[i], M[j]) + cal(M[i], M[k]) + cal(M[j], M[k])
                ans = min(ans, v)
                if ans == 0:
                    return(0)
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    M = list(input().rstrip().split())
    if N >= 48:
        print(0)
    else:
        print(select())