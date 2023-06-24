a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
f = 0 if t <= 30 else (t - 30) * x * 21
f += a
s = 0 if t <= 45 else (t - 45) * y * 21
s += b
print(f, s)