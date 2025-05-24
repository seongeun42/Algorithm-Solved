import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keywords = set()
for _ in range(N):
    keywords.add(input().rstrip())
for _ in range(M):
    use = input().rstrip().split(',')
    for w in use:
        if w in keywords:
            keywords.remove(w)
    print(len(keywords))