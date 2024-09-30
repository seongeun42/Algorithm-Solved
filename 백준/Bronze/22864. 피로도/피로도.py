A, B, C, M = map(int, input().split())
work, tired = 0, 0
for _ in range(24):
    if tired + A > M:
        tired = max(tired - C, 0)
    else:
        tired += A
        work += B
print(work)