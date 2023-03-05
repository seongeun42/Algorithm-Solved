def check(r, c):
    for n in range(5):
            for m in range(5):
                if mo[r][c] == cs[n][m]:
                    row[n] += 1
                    col[m] += 1
                    if n == m:
                        cro[0] += 1
                    if n + m == 4:
                        cro[1] += 1

def binggo():
    for i in range(5):
        for j in range(5):
            check(i, j)
            if row.count(5) + col.count(5) + cro.count(5) >= 3:
                print(i * 5 + j + 1)
                return

cs = [[*map(int, input().split())] for _ in range(5)]
mo = [[*map(int, input().split())] for _ in range(5)]
row = [0] * 5
col = [0] * 5
cro = [0] * 2
binggo()