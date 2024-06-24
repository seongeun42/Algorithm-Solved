import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sori = list(input().split())
    not_fox = set()
    while 1:
        s = input().rstrip()
        if s == "what does the fox say?":
            break
        not_fox.add(list(s.rstrip().split())[-1])
    for v in sori:
        if v not in not_fox:
            print(v, end=" ")
    print()