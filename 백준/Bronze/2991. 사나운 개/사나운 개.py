A, B, C, D = map(int, input().split())
for c in [*map(int, input().split())]:
    cnt = 1 if 0 < c % (A + B) <= A else 0
    cnt += 1 if 0 < c % (C + D) <= C else 0
    print(cnt)