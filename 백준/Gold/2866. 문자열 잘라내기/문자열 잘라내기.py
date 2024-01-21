import sys
input = sys.stdin.readline

def solve():
    R, C = map(int, input().split())
    alpha = [[] for _ in range(C)]
    for _ in range(R):
        s = input().rstrip()
        for i in range(C):
            alpha[i].append(s[i])
    start, end = 0, R - 1
    count = 0
    while start <= end:
        mid = (start + end) // 2
        words = set()
        for i in range(C):
            words.add("".join(alpha[i][mid:]))
        if len(words) == C:
            count = mid
            start = mid + 1
        else:
            end = mid - 1
    print(count)

solve()