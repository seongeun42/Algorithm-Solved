n, w, h, l = map(int, input().split())
res = (w // l) * (h // l)
print(res if res < n else n)