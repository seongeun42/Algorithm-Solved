from collections import deque

def bfs():
    ori = "".join(nums)
    if ori == sort: return 0

    q = deque([(0, ori)])
    visit = set([ori])
    while q:
        ccnt, cnums = q.popleft()
        for i in range(n - k + 1):
            nnums = cnums[0:i] + cnums[i:i + k][::-1] + cnums[i + k:]
            if nnums == sort:
                return ccnt + 1
            if nnums not in visit:
                visit.add(nnums)
                q.append((ccnt + 1, nnums))
    return -1

n, k = map(int, input().split())
nums = list(input().split())
sort = "".join(sorted(nums))
print(bfs())