N, K = map(int, input().split())
multi = [*map(int, input().split())]
cnt = sum([(c + 1) // 2 for c in multi])
print("YES" if N <= cnt else "NO")