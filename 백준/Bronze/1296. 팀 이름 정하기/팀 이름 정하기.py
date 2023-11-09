yd = input()
n = int(input())
names = sorted([input() for _ in range(n)])
ans, score = -1, -1
for i in range(n):
    L = yd.count("L") + names[i].count("L")
    O = yd.count("O") + names[i].count("O")
    V = yd.count("V") + names[i].count("V")
    E = yd.count("E") + names[i].count("E")
    sc = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    if score < sc:
        score = sc
        ans = i
print(names[ans])