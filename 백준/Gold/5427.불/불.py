from collections import deque
import sys, queue

# 정답을 참고했습니다.
## 저는 어렵네요.. ㅎㅎ;;

# Set direction
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS():
    while q:
        x, y = q.popleft()
        if visited[x][y] != 'F':
            flag = visited[x][y]
        else:
            flag = "F"
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col:
                if visited[nx][ny] == 0 and (bldg[nx][ny] == '.' or bldg[nx][ny] == '@'):
                    if flag == "F":
                        visited[nx][ny] = flag
                    else :
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "F":
                    return flag
    return "IMPOSSIBLE"

# Get Param
N = int(input())

# Loop
for _ in range(N):
    col, row = map(int, sys.stdin.readline().split())

    bldg = [] # 빌딩
    q = deque() # 불과 상근의 위치
    visited = [[0] * col for _ in range(row)]
    start = []

    for r in range(row):
        bldg.append(sys.stdin.readline().rstrip())

        # Get F, hero Spot
        for c in range(col):
            if bldg[r][c] == '@':
                visited[r][c] = 1
                start = (r,c)

            elif bldg[r][c] == '*':
                visited[r][c] = 'F'
                q.append((r, c))
        
    q.append(start)
    print(BFS()) 