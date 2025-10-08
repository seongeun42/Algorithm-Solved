import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cow = [[*map(int, input().split())] + [i] for i in range(N)]
print(sorted(sorted(cow, reverse=True)[:K], key=lambda x: -x[1])[0][2] + 1)