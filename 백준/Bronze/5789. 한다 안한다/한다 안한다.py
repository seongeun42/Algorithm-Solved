import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    s = input().rstrip()
    print("Do-it" if s[len(s) // 2 - 1] == s[len(s) // 2] else "Do-it-Not")