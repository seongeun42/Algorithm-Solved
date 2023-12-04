k = int(input())
v = 25 + k * 0.01
if v < 100:
    v = 100
elif v > 2000:
    v = 2000
print(f"{v:.2f}")