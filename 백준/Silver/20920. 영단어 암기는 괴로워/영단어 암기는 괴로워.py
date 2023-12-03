import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = {}
for _ in range(N):
    w = input().rstrip()
    if len(w) < M:
        continue
    if w in words:
        words[w] += 1
    else:
        words[w] = 1
words = list(words.items())
words.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in range(len(words)):
    print(words[i][0])