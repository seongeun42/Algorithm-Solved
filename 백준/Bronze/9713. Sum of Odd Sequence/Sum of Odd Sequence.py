T = int(input())
for _ in range(T):
    N = int(input())
    print(sum([i for i in range(N) if i % 2 == 1]) + N)