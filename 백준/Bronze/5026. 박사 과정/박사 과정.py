import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    s = input().rstrip()
    if s == "P=NP":
        print("skipped")
    else:
        print(sum(map(int, s.split('+'))))