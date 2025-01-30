import sys
input = sys.stdin.readline

for i in range(1, 12001):
    a, cmd, b = input().rstrip().split()
    if cmd == "E":
        break
    if cmd == "!=":
        print(f"Case {i}: {str(int(a) != int(b)).lower()}")
    elif cmd == "<":
        print(f"Case {i}: {str(int(a) < int(b)).lower()}")
    elif cmd == "<=":
        print(f"Case {i}: {str(int(a) <= int(b)).lower()}")
    elif cmd == ">":
        print(f"Case {i}: {str(int(a) > int(b)).lower()}")
    elif cmd == ">=":
        print(f"Case {i}: {str(int(a) >= int(b)).lower()}")
    elif cmd == "==":
        print(f"Case {i}: {str(int(a) == int(b)).lower()}")