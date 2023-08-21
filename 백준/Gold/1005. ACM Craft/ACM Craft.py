from collections import deque
import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        time = [0] + [*map(int, input().split())]
        inG = [[] for _ in range(N + 1)]
        outG = [[] for _ in range(N + 1)]
        degree = [0] * (N + 1)
        for _ in range(K):
            X, Y = map(int, input().split())
            inG[X].append(Y)
            outG[Y].append(X)
            degree[Y] += 1
        
        q = deque([])
        for i in range(1, N + 1):
            if degree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            past = 0
            for v in outG[cur]:
                if past < time[v]:
                    past = time[v]
            time[cur] += past
            for nn in inG[cur]:
                degree[nn] -= 1
                if degree[nn] == 0:
                    q.append(nn)
        print(time[int(input())])

solve()