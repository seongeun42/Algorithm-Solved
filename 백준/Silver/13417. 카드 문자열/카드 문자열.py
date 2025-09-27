from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    alpa = list(input().rstrip().split())
    ans = deque([alpa[0]])
    for i in range(1, N):
        f, c = ord(ans[0]), ord(alpa[i])
        if f < c:
            ans.append(alpa[i])
        else:
            ans.appendleft(alpa[i])
    print(''.join(ans))