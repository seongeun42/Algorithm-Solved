import sys
input = sys.stdin.readline

N = int(input())
mirror = [input().rstrip() for _ in range(N)]
state = int(input())
if state == 1:
    print("\n".join(mirror))
elif state == 2:
    mirror = [s[::-1] for s in mirror]
    print("\n".join(mirror))
else:
    for i in range(N - 1, -1, -1):
        for j in range(N):
            print(mirror[i][j], end="")
        print()