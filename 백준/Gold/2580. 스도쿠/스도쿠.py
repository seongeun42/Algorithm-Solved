def backtrack(cnt):
    # 끝까지 도달하면 True 반환
    if cnt == len(blank):
        for i in range(9):
            print(*sudoqu[i], sep=" ")
        return True
    # 현재 빈칸
    r = blank[cnt][0]
    c = blank[cnt][1]
    # 1~9까지 넣어보기
    for i in range(1, 10):
        # 이미 각 라인과 네모 영역에 있으면 패스
        if row[r][i] or col[c][i] or square[r // 3][c // 3][i]:
            continue
        # 없으면 다음 빈칸 채우러 감
        row[r][i] = True
        col[c][i] = True
        square[r // 3][c // 3][i] = True
        sudoqu[r][c] = i
        if backtrack(cnt + 1): # 끝까지 가서 True 반환되면 중단
            return True
        # 아니면 다른 경우 찾기
        sudoqu[r][c] = 0
        square[r // 3][c // 3][i] = False
        col[c][i] = False
        row[r][i] = False
    return False

# 각 구역 별 있는 숫자
square = [[[False] * 10 for _ in range(3)] for _ in range(3)]
row = [[False] * 10 for _ in range(10)]
col = [[False] * 10 for _ in range(10)]
# 0 위치
blank = []
# 스도쿠 맵
sudoqu = [[] for _ in range(9)]
for i in range(9):
    line = [*map(int, input().split())]
    for j in range(9):
        sudoqu[i].append(line[j])
        if line[j] != 0:
            row[i][line[j]] = True
            col[j][line[j]] = True
            square[i // 3][j // 3][line[j]] = True
        else:
            blank.append((i, j))
backtrack(0)