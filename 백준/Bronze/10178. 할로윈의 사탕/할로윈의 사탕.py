import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    c, v = map(int, input().split())
    div, mod = divmod(c, v)
    print(f"You get {div} piece(s) and your dad gets {mod} piece(s).")