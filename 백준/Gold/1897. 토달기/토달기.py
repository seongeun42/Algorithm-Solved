import sys
input = sys.stdin.readline

def solve():
    d, first = input().split()
    d = int(d)
    words = {}
    for _ in range(d):
        w = input().rstrip()
        words[w] = False
    words[first] = True
    ans = first
    for w in sorted(words.keys(), key=len):
        for i in range(len(w)):
            nw = w[:i] + w[i+1:]
            if nw in words and words[nw]:
                words[w] = True
                if len(ans) < len(w):
                    ans = w
    print(ans)

solve()