import sys
input = sys.stdin.readline

i = 0
while 1:
    i += 1
    rwl = [*map(int, input().split())]
    if len(rwl) == 1:
        break
    print(f"Pizza {i} {'fits' if rwl[1] ** 2 + rwl[2] ** 2 <= (rwl[0] * 2) ** 2 else 'does not fit'} on the table.")