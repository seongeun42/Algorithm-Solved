import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

N = int(input())
cow = [[*map(int, input().split())] for _ in range(N)]
E = []
for i in range(N):
    for j in range(i + 1, N):
        dist = (cow[i][0] - cow[j][0]) ** 2 + (cow[i][1] - cow[j][1]) ** 2
        E.append((dist, i, j))
E.sort()
R = [i for i in range(N)]
ans = 0
cnt = 1
for cost, i, j in E:
    if cnt == N:
        break
    ir = find_root(i)
    jr = find_root(j)
    if ir != jr:
        ans = cost
        cnt += 1
        R[max(ir, jr)] = min(ir, jr)
print(ans)