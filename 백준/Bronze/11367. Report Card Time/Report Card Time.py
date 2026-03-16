import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    name, score = input().rstrip().split()
    score = int(score)
    if 97 <= score:
        score = "A+"
    elif 90 <= score:
        score = "A"
    elif 87 <= score:
        score = "B+"
    elif 80 <= score:
        score = "B"
    elif 77 <= score:
        score = "C+"
    elif 70 <= score:
        score = "C"
    elif 67 <= score:
        score = "D+"
    elif 60 <= score:
        score = "D"
    else:
        score = "F"
    print(name, score)