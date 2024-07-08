import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
cnt = {}
for word in words:
    for i in range(len(word)):
        cnt[word[i]] = cnt.get(word[i], 0) + 10 ** (len(word) - i - 1)
cnt = sorted(cnt.values(), reverse=True)
print(sum([cnt[i] * (9 - i) for i in range(len(cnt))]))