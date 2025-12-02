R, G, B = map(int, input().split())
box = min(R, G, B)
R, G, B = R - box, G - box, B - box
for i in range(3, 1, -1):
    box += R // i + G // i + B // i
    R, G, B = R % i, G % i, B % i
box += max(R, G, B)
print(box)