t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())
maxT = 3 * t1 + 20 * e1 + 120 * f1
melT = 3 * t2 + 20 * e2 + 120 * f2
if maxT > melT:
    print("Max")
elif maxT < melT:
    print("Mel")
else:
    print("Draw")