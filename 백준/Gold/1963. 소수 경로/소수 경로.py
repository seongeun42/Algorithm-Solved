from collections import deque
import sys
input = sys.stdin.readline

sosu = [True] * 100000
sosu[0], sosu[1] = False, False
for i in range(2, int(100000**0.5)):
    if sosu[i]:
        for j in range(i + i, 100000, i):
            sosu[j] = False

def solve():
    T = int(input())
    for _ in range(T):
        A, B = map(list, input().split())
        visited = [0] * 100000
        visited[int(''.join(A))] = 1
        q = deque([A])
        while q:
            cur = q.popleft()
            if cur == B:
                break
            for i in range(4):
                for j in "0123456789":
                    if cur[i] == j:
                        continue
                    nxt = cur[:]
                    nxt[i] = j
                    num = int(''.join(nxt))
                    if num >= 1000 and visited[num] == 0 and sosu[num]:
                        visited[num] = visited[int(''.join(cur))] + 1
                        q.append(nxt)
        cnt = visited[int(''.join(B))]
        print(cnt - 1 if cnt > 0 else "Impossible")

solve()