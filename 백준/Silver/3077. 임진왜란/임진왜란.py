import sys
input = sys.stdin.readline

N = int(input())
correct = {v: i for i, v in enumerate(input().rstrip().split())}
hw = list(input().rstrip().split())
all = N * (N - 1) // 2
score = 0
for i in range(N):
    for j in range(i + 1, N):
        if correct[hw[i]] < correct[hw[j]]:
            score += 1
print(f"{score}/{all}")