import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    print(f"Case #{t + 1}:", max([*map(int, input().split())]))