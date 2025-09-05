import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    P = [*map(int, input().split())]
    P_sort = sorted([(i, v) for i, v in enumerate(P)], key=lambda x: (x[1], -x[0]))
    M = int(input())
    if N == 1:
        print(0)
        return
    room = []
    if P_sort[0][0] == 0:
        room.append(P_sort[1][0])
        M -= P_sort[1][1]
        if M < 0:
            print(0)
            return
        room.extend([0] * (M // P_sort[0][1]))
        M -= P_sort[0][1] * (len(room) - 1)
    else:
        room.extend([P_sort[0][0]] * (M // P_sort[0][1]))
        M -= P_sort[0][1] * len(room)
    for i in range(len(room)):
        if M == 0:
            break
        for j in range(N - 1, -1, -1):
            if i == 0 and P_sort[0][0] == 0:
                term = P[j] - P_sort[1][1]
            else:
                term = P[j] - P_sort[0][1]
            if term <= M:
                room[i] = j
                M -= term
                break
    ans = 0
    for v in room:
        ans = ans * 10 + v
    print(ans)

solve()