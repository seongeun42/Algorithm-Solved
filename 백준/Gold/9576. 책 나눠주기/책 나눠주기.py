import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        ab = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: x[1])
        # 0~i번까지 범위 내에서 가져갈 수 있는 책 중 가장 큰 값 기록
        R = [i for i in range(N + 2)]
        ans = 0
        for i in range(M):
            s, e = ab[i]
            # 앞에서부터 가져갈 수 있는 책 찾기
            enable_book = find_root(s, R)
            # 신청 범위 내면 책 주기
            if s <= enable_book <= e:
                ans += 1
                # 준 책의 다음 번호 기록
                R[enable_book] += 1
        print(ans)

solve()