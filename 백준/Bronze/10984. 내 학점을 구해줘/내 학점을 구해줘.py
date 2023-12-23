T = int(input())
for _ in range(T):
    N = int(input())
    totalC, totalG = 0, 0
    for _ in range(N):
        C, G = map(float, input().split())
        totalC += C
        totalG += G * C
    print(int(totalC), f"{totalG / totalC:.1f}")