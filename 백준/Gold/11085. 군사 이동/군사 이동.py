import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

p, w = map(int, input().split())
c, v = map(int, input().split())
R = [i for i in range(p)]
E = []
for _ in range(w):
    ws, we, ww = map(int, input().split())
    E.append((ww, ws, we))
E.sort(key=lambda x: -x[0])
ans = 1001
for ww, ws, we in E:
    if find_root(R[c]) == find_root(R[v]):
        break
    r_ws = find_root(ws)
    r_we = find_root(we)
    if r_ws != r_we:
        R[max(r_ws, r_we)] = min(r_ws, r_we)
        if min(r_ws, r_we) == find_root(R[c]) and ans > ww:
            ans = ww
print(ans)