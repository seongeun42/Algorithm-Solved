import math

s, t = input(), input()
lcm = math.lcm(len(s), len(t))
print(1 if s * (lcm // len(s)) == t * (lcm // len(t)) else 0)