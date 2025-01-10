import sys
input = sys.stdin.readline

def solve():
    N, type = input().rstrip().split()
    N = int(N)
    people = {input().rstrip() for _ in range(N)}
    need = {"Y": 1, "F": 2, "O": 3}
    print(len(people) // need[type])

solve()