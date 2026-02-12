import sys
input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N):
    w = input().rstrip()
    if len(words) == 0:
        words.add(w)
    else:
        for i in range(len(w)):
            if ''.join(w[i:] + w[:i]) in words:
                break
        else:
            words.add(w)
print(len(words))