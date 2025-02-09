import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    nums = [[*map(int, list(input().rstrip()))] for _ in range(N)]
    psum = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            psum[i][j] = nums[i - 1][j - 1] + psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1]
    ans = 0
    # 3개 넓이 구하기 - ㅏ, ㅗ, ㅓ, ㅜ
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            lu = psum[i][j]
            lb = psum[N][j] - lu
            ru = psum[i][M] - lu
            rb = psum[N][M] - lu - lb - ru
            ans = max((lu + lb) * ru * rb, lu * ru * (lb + rb), lu * lb * (ru + rb), (lu + ru) * lb * rb, ans)
    # 3개 넓이 구하기 - =
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            one = psum[i][M]
            two = psum[j][M] - one
            third = psum[N][M] - one - two
            ans = max(ans, one * two * third)
    # 3개 넓이 구하기 - ll
    for i in range(1, M - 1):
        for j in range(i + 1, M):
            one = psum[N][i]
            two = psum[N][j] - one
            third = psum[N][M] - one - two
            ans = max(ans, one * two * third)
    print(ans)

solve()