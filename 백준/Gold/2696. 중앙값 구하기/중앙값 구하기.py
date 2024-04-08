import sys, heapq
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        M = int(input())
        nums = []
        for _ in range(M // 10 + 1):
            nums += [*map(int, input().split())]
        maxH, minH = [], []
        ans = []
        for i in range(M):
            if i % 2 == 0:
                heapq.heappush(maxH, -nums[i])
            else:
                heapq.heappush(minH, nums[i])
            if minH and -maxH[0] >= minH[0]:
                maxHR = -heapq.heappop(maxH)
                minHR = heapq.heappop(minH)
                heapq.heappush(maxH, -minHR)
                heapq.heappush(minH, maxHR)
            if i % 2 == 0:
                ans.append(-maxH[0])
        print(len(ans))
        for i in range(len(ans) // 10 + 1):
            print(*ans[i*10:i*10+10])
    
solve()