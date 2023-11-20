import sys
input = sys.stdin.readline

n = int(input())
scores = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: -x[2])
nation = scores[0][0] == scores[1][0]
print(scores[0][0], scores[0][1])
print(scores[1][0], scores[1][1])
for i in range(2, n):
    if (not nation) or (nation and scores[i][0] != scores[0][0]):
        print(scores[i][0], scores[i][1])
        break