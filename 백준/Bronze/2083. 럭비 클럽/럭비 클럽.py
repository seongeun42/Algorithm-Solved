import sys
input = sys.stdin.readline

while 1:
    n, a, w = input().split()
    if n == "#" and a == "0" and w == "0":
        break
    if int(a) > 17 or int(w) >= 80:
        print(n, "Senior")
    else:
        print(n, "Junior")