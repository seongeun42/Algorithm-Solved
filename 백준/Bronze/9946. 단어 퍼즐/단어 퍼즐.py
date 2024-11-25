import sys
input = sys.stdin.readline

def solve():
    i = 1
    while i:
        a, b = input().rstrip(), input().rstrip()
        if a == b == "END":
            break
        print(f"Case {i}: {'same' if sorted(a) == sorted(b) else 'different'}")
        i += 1

solve()