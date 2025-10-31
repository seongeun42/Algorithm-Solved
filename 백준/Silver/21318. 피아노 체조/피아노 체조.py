import sys
input = sys.stdin.readline

N = int(input())
music = [0] + [*map(int, input().split())]
mistake = [0]
for i in range(1, N):
    mistake.append(mistake[-1] + (1 if music[i] > music[i + 1] else 0))
mistake.append(mistake[-1])
Q = int(input())
for q in range(Q):
    x, y = map(int, input().split())
    ans = mistake[y] - mistake[x - 1]
    if y < N and music[y] > music[y + 1]:
        ans -= 1
    print(ans)