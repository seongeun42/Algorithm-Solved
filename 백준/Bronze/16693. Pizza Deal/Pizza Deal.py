from math import pi
a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())
o = p1 / a1
t = p2 / (r1 ** 2 * pi)
print("Whole pizza" if o > t else "Slice of pizza")