A, B, C = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())
if B:
    coordi = [(x1, y1), (x2, y2)] if A / B > 0 else [(x1, y2), (x2, y1)]
else:
    coordi = [(x1, y1), (x2, y2)]
v1 = A * coordi[0][0] + B * coordi[0][1] + C
v2 = A * coordi[1][0] + B * coordi[1][1] + C
if (v1 < 0 and v2 > 0) or (v1 > 0 and v2 < 0):
    print("Poor")
else:
    print("Lucky")