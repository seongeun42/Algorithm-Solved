import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    U = sorted([int(input()) for _ in range(N)])
    hap = []
    for i in range(N):
        for j in range(i, N):
            hap.append(U[i] + U[j])
    hap.sort()
    for i in range(N - 1, -1, -1):
        for j in range(i, -1, -1):
            target = U[i] - U[j]
            s, e = 0, len(hap) - 1
            while s <= e:
                mid = (s + e) // 2
                if hap[mid] == target:
                    return U[i]
                elif hap[mid] > target:
                    e = mid - 1
                else:
                    s = mid + 1

print(solve())