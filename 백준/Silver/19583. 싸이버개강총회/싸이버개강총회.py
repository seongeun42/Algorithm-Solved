import sys
input = sys.stdin.readline

S, E, Q = input().rstrip().split()
S = [*map(int, S.split(':'))]
E = [*map(int, E.split(':'))]
Q = [*map(int, Q.split(':'))]
S, E, Q = S[0] * 60 + S[1], E[0] * 60 + E[1], Q[0] * 60 + Q[1]
in_m, out_m = set(), set()
while 1:
    line = input().rstrip()
    if not line:
        break
    time, name = line.split()
    time = [*map(int, time.split(':'))]
    time = time[0] * 60 + time[1]
    if 0 <= time <= S:
        in_m.add(name)
    elif E <= time <= Q:
        out_m.add(name)
print(len(in_m & out_m))