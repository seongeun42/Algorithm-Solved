import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    name = input().rstrip()
    g = b = 0
    for c in name:
        if c in "Gg":
            g += 1
        elif c in "Bb":
            b += 1
    if g == b:
        print(f"{name} is NEUTRAL")
    else:
        print(f"{name} is {'GOOD' if g > b else 'A BADDY'}")