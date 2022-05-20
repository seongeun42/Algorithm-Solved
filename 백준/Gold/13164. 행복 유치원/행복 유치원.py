N, K = map(int, input().split())
tall = [*map(int, input().split())]
cha = sorted([tall[i + 1] - tall[i] for i in range(N - 1)])
print(sum(cha[:N - K]))