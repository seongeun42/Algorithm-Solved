import sys
input = sys.stdin.readline

N = int(input())
score = sorted([float(input()) for _ in range(N)])
for v in score[:7]:
    print(f"{v:.3f}")