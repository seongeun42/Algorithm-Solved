from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split()) 
    names = deque([input().rstrip() for _ in range(N)])
    ans = 0
    cnt = [0] * 21
    for i in range(K + 1):
        cnt[len(names[i])] += 1
    for i in range(21):
        ans += cnt[i] * (cnt[i] - 1) // 2
    while len(names) > K + 1:
        cnt[len(names[0])] -= 1
        names.popleft()
        name = len(names[K])
        ans += cnt[name]
        cnt[name] += 1
    print(ans)

solve()