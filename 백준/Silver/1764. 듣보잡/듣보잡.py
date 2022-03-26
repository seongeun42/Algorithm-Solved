import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dm = set([input().strip() for _ in range(N)])
bm = set([input().strip() for _ in range(M)])
ans = sorted(list(dm & bm))
print(len(ans))
print("\n".join(ans))