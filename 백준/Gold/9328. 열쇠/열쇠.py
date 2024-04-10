from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def check(c, q, i, j, visited, keys, lock):
    visited[i][j] = True
    # 빈칸이면 추가
    if c == '.':
        q.append((i, j))
    # 문이면
    elif 'A' <= c <= 'Z':
        # 열쇠 있으면 추가
        if keys[chr(ord(c) + 32)]:
            q.append((i, j))
        else: # 없으면 닫힌 문에 기록
            lock[c].append((i, j))
    # 열쇠면 줍고, 닫혔던 문 열기
    elif 'a' <= c <= 'z':
        keys[c] = True
        q.append((i, j))
        for door in lock[chr(ord(c) - 32)]:
            q.append(door)
    # 문서면 훔치고 추가
    elif c == '$':
        q.append((i, j))
        return 1
    return 0

def solve():
    T = int(input())
    for _ in range(T):
        h, w = map(int, input().split())
        arr = [list(input().rstrip()) for _ in range(h)]
        # 가진 열쇠 기록
        keys = {chr(97 + i): False for i in range(26)}
        for c in input().rstrip():
            if c == '0':
                break
            keys[c] = True

        ans = 0
        # 입구 찾기
        q = deque([])
        visited = [[False] * w for _ in range(h)]
        # 열쇠 없어서 못 연 문 기록
        lock = {chr(65 + i): [] for i in range(26)}
        for i in [0, h - 1]:
            for j in range(w):
                ans += check(arr[i][j], q, i, j, visited, keys, lock)
        for i in range(1, h - 1):
            for j in [0, w - 1]:
                ans += check(arr[i][j], q, i, j, visited, keys, lock)
        
        while q:
            cy, cx = q.popleft() 
            for d in range(4):
                ny, nx = cy + dr[d], cx + dc[d]
                if 0 <= ny < h and 0 <= nx < w and arr[ny][nx] != '*' and not visited[ny][nx]:
                    ans += check(arr[ny][nx], q, ny, nx, visited, keys, lock)
        print(ans)

solve()