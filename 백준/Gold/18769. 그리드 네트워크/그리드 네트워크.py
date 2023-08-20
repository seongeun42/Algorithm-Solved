import sys
input = sys.stdin.readline

def find_root(node, root):
    if root[node] != node:
        root[node] = find_root(root[node], root)
    return root[node]

def solve():
    T = int(input())
    for _ in range(T):
        R, C = map(int, input().split())
        root = [i for i in range(R * C)]
        ans = 0
        E = []
        for i in range(R):
            c = [*map(int, input().split())]
            for j in range(C - 1):
                a = i * C + j
                b = a + 1
                ar = find_root(a, root)
                br = find_root(b, root)
                if c[j] == 1 and ar != br:
                    root[max(ar, br)] = min(ar, br)
                    ans += 1
                elif c[j] != 1:
                    E.append((c[j], a, b))
        for i in range(R - 1):
            c = [*map(int, input().split())]
            for j in range(C):
                a = i * C + j
                b = a + C
                ar = find_root(a, root)
                br = find_root(b, root)
                if c[j] == 1 and ar != br:
                    root[max(ar, br)] = min(ar, br)
                    ans += 1
                elif c[j] != 1:
                    E.append((c[j], a, b))
        E.sort()
        for w, a, b in E:
            if len(set(root)) == 1: break
            ar = find_root(a, root)
            br = find_root(b, root)
            if ar != br:
                ans += w
                root[max(ar, br)] = min(ar, br)
        print(ans)

solve()