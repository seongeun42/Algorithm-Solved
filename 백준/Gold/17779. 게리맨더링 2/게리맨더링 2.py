import sys
input = sys.stdin.readline

def is_in_range(y, x, d1, d2, N):
    if not (0 < y <= N and 0 < x <= N):
        return False
    if not (0 < y - d1 <= N and 0 < x + d1 <= N):
        return False
    if not (0 < y + d2 <= N and 0 < x + d2 <= N):
        return False
    if not (0 < y - d1 + d2 <= N and 0 < x + d1 + d2 <= N):
        return False
    return True

def solve():
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    # 인구 행단위 누적합
    prefix = [[0] * (N + 1) for _ in range(N + 1)]
    total = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix[i][j] = arr[i - 1][j - 1] + prefix[i][j - 1]
        total += prefix[i][N]
    # x, y, d1, d2 모든 경우 체크
    ans = 40000
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    # 유효한 범위인 경우만 인구수 체크
                    if is_in_range(y, x, d1, d2, N):
                        # 1구역
                        one = 0
                        for i in range(y - 1, 0, -1):
                            diff = -(i - y + 1)
                            one += prefix[i][min(x + diff, x + d1)]
                        # 2구역
                        two = 0
                        for i in range(y - d1 + d2, 0, -1):
                            diff = -(i - y + d1 - d2)
                            two += prefix[i][N] - prefix[i][max(x + d1 + d2 - diff, x + d1)]
                        # 3구역
                        three = 0
                        for i in range(y, N + 1):
                            diff = i - y
                            three += prefix[i][min(x - 1 + diff, x + d2 - 1)]
                        # 4구역
                        four = 0
                        for i in range(y - d1 + d2 + 1, N + 1):
                            diff = i - y + d1 - d2 - 1
                            four += prefix[i][N] - prefix[i][max(x + d2 + d1 - 1 - diff, x + d2 - 1)]
                        # 5구역
                        five = total - one - two - three - four
                        diff = max(one, two, three, four, five) - min(one, two, three, four, five)
                        if diff < ans:
                            ans = diff
    print(ans)

solve()