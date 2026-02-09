import sys
input = sys.stdin.readline

def getCnt(stack, height):
    cnt = 0
    cur = 500001
    while stack and stack[-1][1] > height:
        nxt = stack.pop()[1]
        if nxt < cur:
            cnt += 1
            cur = nxt
    return cnt

def solve():
    n = int(input())
    stack = []
    cnt = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if stack and stack[-1][1] > y:
            cnt += getCnt(stack, y)
        if y != 0:
            stack.append((x, y))
    if stack:
        cnt += getCnt(stack, 0)
    print(cnt)

solve()