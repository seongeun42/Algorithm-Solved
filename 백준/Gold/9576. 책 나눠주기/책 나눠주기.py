import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, visited, ab, book):
    # x 학생의 책 신청 범위
    s, e = ab[x]
    for i in range(s - 1, e):
        # 체크한 적 있으면 패스
        if visited[i]:
            continue
        # 없으면 체크
        visited[i] = True
        # i번 책이 남아 있거나, i번 책 가져간 다른 학생이 책을 바꿀 수 있으면 책 주기
        if book[i] == -1 or dfs(book[i], visited, ab, book):
            book[i] = x
            return True
    return False

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        # 책이 누구에게 갔는지
        book = [-1] * (N + 1)
        # 범위 좁은 순으로 정렬
        ab = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: (x[1] - x[0]))
        matched = 0
        for i in range(M):
            visited = [False] * (N + 1)
            if dfs(i, visited, ab, book):
                matched += 1
        print(matched)

solve()