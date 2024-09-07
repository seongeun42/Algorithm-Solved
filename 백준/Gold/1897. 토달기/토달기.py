from collections import deque
import sys
input = sys.stdin.readline

def solve():
    d, first = input().split()
    d = int(d)
    words = {}
    for _ in range(d):
        w = input().rstrip()
        if len(w) in words:
            words[len(w)].append(w)
        else:
            words[len(w)] = [w]
    q = deque([first])
    ans = first
    while q:
        word: str = q.popleft()
        if len(ans) < len(word):
            ans = word
        for w in words.get(len(word) + 1, []):
            diff = 0
            idx = 0
            for i in range(len(w)):
                if idx >= len(word) or w[i] != word[idx]:
                    diff += 1
                else:
                    idx += 1
            if diff == 1:
                q.append(w)
    print(ans)

solve()