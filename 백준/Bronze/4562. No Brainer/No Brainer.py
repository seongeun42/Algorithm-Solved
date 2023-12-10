N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    print("NO BRAINS" if X < Y else "MMM BRAINS")