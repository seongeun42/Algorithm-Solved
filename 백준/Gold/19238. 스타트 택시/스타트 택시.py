from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def find_passenger(arr, taxi, N, passengers, priority):
    q = deque([taxi])
    visited = [[0] * N for _ in range(N)]
    visited[taxi[0]][taxi[1]] = 1
    pick = (-1, -1)
    need_fuel = 401
    while q:
        cr, cc = q.popleft()
        if (cr, cc) in passengers and passengers[(cr, cc)] != 0:
            if visited[cr][cc] < need_fuel or (visited[cr][cc] == need_fuel and priority[(cr, cc)] < priority[pick]):
                pick = (cr, cc)
                need_fuel = visited[cr][cc]
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] == 0:
                visited[nr][nc] = visited[cr][cc] + 1
                q.append([nr, nc])
    return pick, need_fuel - 1

def predict_fuel(arr, taxi, dest, N):
    q = deque([taxi])
    visited = [[0] * N for _ in range(N)]
    visited[taxi[0]][taxi[1]] = 1
    while q:
        cr, cc = q.popleft()
        if (cr, cc) == dest:
            return visited[cr][cc] - 1
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] == 0:
                visited[nr][nc] = visited[cr][cc] + 1
                q.append([nr, nc])
    return -1

def solve():
    N, M, fuel = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(N)]
    passengers = {}
    tr, tc = map(int, input().split())
    taxi = [tr - 1, tc - 1]
    for _ in range(M):
        sr, sc, er, ec = map(int, input().split())
        passengers[(sr - 1, sc - 1)] = (er - 1, ec - 1)
    tmp = sorted(passengers.keys(), key=lambda x: (x[0], x[1]))
    priority = {key: val for val, key in enumerate(tmp)}
    remain = M
    while remain > 0:
        passenger, need_fuel = find_passenger(arr, taxi, N, passengers, priority)
        if fuel < need_fuel or passenger == (-1, -1):
            print(-1)
            return
        taxi = passenger
        fuel -= need_fuel
        move_need_fuel = predict_fuel(arr, taxi, passengers[passenger], N)
        if move_need_fuel == -1 or fuel < move_need_fuel:
            print(-1)
            return
        taxi, passengers[passenger] = passengers[passenger], 0
        fuel += move_need_fuel
        remain -= 1
    print(fuel)

solve()