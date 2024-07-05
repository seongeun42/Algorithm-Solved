from collections import deque
import sys
input = sys.stdin.readline

def bfs(T, xy):
    q = deque([(0, 0, 0)])
    visit = set([(0, 0)])
    while q:
        cx, cy, cnt = q.popleft()
        if cy == T:
            return cnt
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = cx + i, cy + j
                if (nx, ny) in xy and (nx, ny) not in visit:
                    visit.add((nx, ny))
                    q.append((nx, ny, cnt + 1))
    return -1

def solve():
    n, T = map(int, input().split())
    xy = set([tuple(map(int, input().split())) for _ in range(n)])
    print(bfs(T, xy))
    
solve()