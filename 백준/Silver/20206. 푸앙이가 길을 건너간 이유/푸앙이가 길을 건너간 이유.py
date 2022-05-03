A, B, C = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())
xy = [(x1, y1), (x2, y2)] if B and A / B > 0 else [(x1, y2), (x2, y1)]
v1 = A * xy[0][0] + B * xy[0][1] + C
v2 = A * xy[1][0] + B * xy[1][1] + C
print("Poor" if v2 and v1 / v2 < 0 else "Lucky")