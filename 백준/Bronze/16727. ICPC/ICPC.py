p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
if p1 + p2 == s1 + s2:
    if s1 == p2:
        print("Penalty")
    else:
        print("Esteghlal" if s1 > p2 else "Persepolis")
else:
    print("Esteghlal" if s1 + s2 > p1 + p2 else "Persepolis")