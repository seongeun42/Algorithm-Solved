import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

N = int(input())
A, a = ord('A'), ord('a')
E = []
for i in range(N):
    s = input().strip()
    for j in range(N):
        if s[j] == '0':
            continue
        v = ord(s[j]) - a + 1 if s[j].islower() else ord(s[j]) - A + 27
        E.append((i, j, v))
E.sort(key=lambda x: x[2])

R = [i for i in range(N)]
total, use = 0, 0
for i, j, v in E:
    total += v
    ir = find_root(i)
    jr = find_root(j)
    if ir != jr:
        use += v
        R[max(ir, jr)] = min(ir, jr)

for i in range(N):
    find_root(i)

print(total - use if len(set(R)) == 1 else -1)