N = int(input())
scores = []
for _ in range(N):
    a, d, g = map(int, input().split())
    s = a * (d + g)
    scores.append(s if a != d + g else s * 2)
print(max(scores))