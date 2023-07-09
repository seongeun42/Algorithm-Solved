T = int(input())
for _ in range(T):
    n = sorted([i for i in [*map(int, input().split())] if i % 2 == 0])
    print(sum(n), n[0])