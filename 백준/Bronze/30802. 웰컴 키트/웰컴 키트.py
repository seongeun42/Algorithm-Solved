import math
N = int(input())
cnt = [*map(int, input().split())]
T, P = map(int, input().split())
print(sum([math.ceil(v / T) for v in cnt]))
print(*divmod(N, P))