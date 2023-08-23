def backtrack(cnt):
    if cnt == len(blank):
        for i in range(9):
            print(*sudoqu[i], sep="")
        return True
    r = blank[cnt][0]
    c = blank[cnt][1]
    sIdx = (r // 3) * 3 + c // 3
    for i in range(1, 10):
        if i in row[r] or i in col[c] or i in square[sIdx]:
            continue
        row[r].add(i)
        col[c].add(i)
        square[sIdx].add(i)
        sudoqu[r][c] = i
        if backtrack(cnt + 1):
            return True
        sudoqu[r][c] = 0
        square[sIdx].remove(i)
        col[c].remove(i)
        row[r].remove(i)
    return False

square = [set() for _ in range(9)]
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
blank = []
sudoqu = [[] for _ in range(9)]
for i in range(9):
    line = [*map(int, str(input()))]
    for j in range(9):
        sudoqu[i].append(line[j])
        if line[j] != 0:
            row[i].add(line[j])
            col[j].add(line[j])
            square[(i // 3) * 3 + j // 3].add(line[j])
        else:
            blank.append((i, j))
backtrack(0)