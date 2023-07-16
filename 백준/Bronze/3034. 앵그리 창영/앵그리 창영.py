n, w, h = map(int, input().split())
l = max([w, h, int((w * w + h * h) ** 0.5)])
for _ in range(n):
    v = int(input())
    print("DA" if v <= l else "NE")