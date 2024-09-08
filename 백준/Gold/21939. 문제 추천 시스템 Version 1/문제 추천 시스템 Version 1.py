import sys, heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    level = {}
    problem = {}
    for _ in range(N):
        P, L = map(int, input().split())
        problem[P] = L
        if L in level:
            minHQ, maxHQ = level[L]
            heapq.heappush(minHQ, P)
            heapq.heappush(maxHQ, -P)
        else:
            minHQ, maxHQ = [P], [-P]
            level[L] = [minHQ, maxHQ]
    M = int(input())
    remove = set()
    for _ in range(M):
        cmd = input().rstrip().split()
        if cmd[0] == "recommend":
            sorted_level = sorted(level.keys())
            if cmd[1] == "1":
                for i in range(len(sorted_level) - 1, -1, -1):
                    maxHQ = level[sorted_level[i]][1]
                    while maxHQ and -maxHQ[0] + sorted_level[i] * 1000000 in remove:
                        heapq.heappop(maxHQ)
                    if maxHQ:
                        print(-maxHQ[0])
                        break
            else:
                for i in range(len(sorted_level)):
                    minHQ = level[sorted_level[i]][0]
                    while minHQ and minHQ[0] + sorted_level[i] * 1000000 in remove:
                        heapq.heappop(minHQ)
                    if minHQ:
                        print(minHQ[0])
                        break
        elif cmd[0] == "add":
            p, l = int(cmd[1]), int(cmd[2])
            problem[p] = l
            if p + l * 1000000 in remove:
                remove.remove(p + l * 1000000)
            if l in level:
                minHQ, maxHQ = level[l]
                heapq.heappush(minHQ, p)
                heapq.heappush(maxHQ, -p)
            else:
                minHQ, maxHQ = [p], [-p]
                level[l] = [minHQ, maxHQ]
        elif cmd[0] == "solved":
            target = int(cmd[1])
            remove.add(target + problem[target] * 1000000)

solve()