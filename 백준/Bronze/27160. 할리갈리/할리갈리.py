from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    f, k = input().rstrip().split()
    cnt[f] += int(k)
print("YES" if 5 in cnt.values() else "NO")