wc, hc, ws, hs = map(int, input().split())
print(1 if ws < wc - 1 and hs < hc - 1 else 0)