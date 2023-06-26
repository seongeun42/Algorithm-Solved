n = int(input())
for _ in range(n):
    d, f, m = map(float, input().split())
    print(f"${d * f * m:.2f}")