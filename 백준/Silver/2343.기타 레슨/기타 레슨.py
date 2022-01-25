import sys

input = sys.stdin.readline


def condition(key):
    cnt = 1
    sub = 0
    for time in lesson:
        sub += time
        if sub > key:
            sub = time
            cnt += 1

    return cnt <= M


N, M = map(int, input().split())
lesson = list(map(int, input().split()))
low, high = max(lesson), sum(lesson)

while low <= high:
    mid = (low + high) // 2

    if condition(mid):
        high = mid - 1
    else:
        low = mid + 1
print(low)