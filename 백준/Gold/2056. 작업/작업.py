import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    time = [0] * (N + 1)
    for i in range(N):
        task = [*map(int, input().split())]
        time[i + 1] = task[0]
        if task[1] != 0:
            past = 0
            for j in range(2, len(task)):
                if past < time[task[j]]:
                    past = time[task[j]]
            time[i + 1] += past
    print(max(time))

solve()