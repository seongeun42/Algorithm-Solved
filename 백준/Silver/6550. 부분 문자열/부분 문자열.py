import sys
input = sys.stdin.readline

while 1:
    try:
        s, t = input().rstrip().split()
        idx = 0
        for c in s:
            while idx < len(t) and c != t[idx]:
                idx += 1
            if idx >= len(t):
                print("No")
                break
            if c == t[idx]:
                idx += 1
        else:
            print("Yes")
    except Exception:
        break