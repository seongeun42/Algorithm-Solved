p = [int(input()) for _ in range(4)]
if p[0] == p[1] == p[2] == p[3]:
    print("Fish At Constant Depth")
elif p[0] < p[1] < p[2] < p[3]:
    print("Fish Rising")
elif p[0] > p[1] > p[2] > p[3]:
    print("Fish Diving")
else:
    print("No Fish")