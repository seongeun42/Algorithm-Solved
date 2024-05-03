import sys
input = sys.stdin.readline

def solve():
    N, M, L, K = map(int, input().split())
    star = []
    for _ in range(K):
        x, y = map(int, input().split())
        star.append((x, y))
    # 2개의 별똥별을 기준으로 개수 세기
    ans = 0
    for sc, sr in star:
        for ec, er in star:
            cnt = 0
            for c, r in star:
                if sc <= c <= sc + L and er <= r <= er + L:
                    cnt += 1
            if ans < cnt:
                ans = cnt
    print(K - ans)

solve()