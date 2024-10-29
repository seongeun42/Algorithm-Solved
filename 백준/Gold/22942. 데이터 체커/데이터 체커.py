import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    lr = []
    for _ in range(N):
        x, r = map(int, input().split())
        lr.append((x - r, x + r))
    lr.sort()
    stack = [lr[0]]
    i = 1
    while i < N:
        while i < N and stack and stack[-1][0] < lr[i][0] and lr[i][1] < stack[-1][1]:
            stack.append(lr[i])
            i += 1
        if i == N:
            break
        if stack:
            l, r = stack.pop()
            if lr[i][0] <= r:
                return "NO"
        else:
            stack.append(lr[i])
            i += 1
    return "YES"

print(solve())