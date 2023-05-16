import sys
input = sys.stdin.readline

def find_root(node):
    if R[node] != node:
        R[node] = find_root(R[node])
    return R[node]

n = int(input())
star = [[*map(float, input().split())] for _ in range(n)]
E = []
for i in range(n - 1):
    for j in range(i + 1, n):
        dist = ((star[i][0] - star[j][0]) ** 2 + (star[i][1] - star[j][1]) ** 2) ** 0.5
        E.append((dist, i, j))
        E.append((dist, j, i))
E.sort()

R = [i for i in range(n)]
ans = 0
for w, s, e in E:
    sr = find_root(s)
    er = find_root(e)
    if sr != er:
        ans += w
        if sr < er:
            R[er] = sr
        else:
            R[sr] = er

print(round(ans, 2))