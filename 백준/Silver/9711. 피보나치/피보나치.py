import sys
input = sys.stdin.readline

T = int(input())
fi = [1, 1]
for i in range(2, 10001):
    fi.append(fi[i - 2] + fi[i - 1])
for t in range(T):
    P, Q = map(int, input().split())
    print(f"Case #{t + 1}: {fi[P - 1] % Q}")