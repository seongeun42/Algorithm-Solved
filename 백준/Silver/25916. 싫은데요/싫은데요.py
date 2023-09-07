import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [*map(int, input().split())]
    if N == 1:
        print(0 if A[0] > M else A[0])
        exit(0)
    s, e = 0, 1
    ans = 0
    total = A[0] if A[0] <= M else 0
    while s <= e and e <= N - 1:
        if total + A[e] <= M:
            total += A[e]
            e += 1
        elif total + A[e] > M:
            if A[e] > M and e + 1 <= N - 1:
                s = e + 1
                e += 1
                total = 0
            else:
                total -= A[s]
                s += 1
        if ans < total:
            ans = total
    print(ans)