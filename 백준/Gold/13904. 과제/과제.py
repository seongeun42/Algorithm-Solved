import sys, heapq
input = sys.stdin.readline

def find_day(days, cur):
    if days[cur] == cur:
        return cur
    days[cur] = find_day(days, days[cur])
    return days[cur]

def solve():
    N = int(input())
    homework = []
    for _ in range(N):
        d, w = map(int, input().split())
        heapq.heappush(homework, (-w, d))
    days = list(range(1001))
    scores = 0
    while homework:
        w, d = heapq.heappop(homework)
        w = -w
        day = find_day(days, d)
        if day > 0:
            null_day = find_day(days, day - 1)
            days[day] = null_day
            scores += w
    print(scores)

solve()