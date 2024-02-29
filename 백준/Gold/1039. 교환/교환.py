from collections import deque

def bfs(N, K, size):
    q = deque([(N, 0)])
    visited = [-1] * 1000001
    ans = -1
    while q:
        num, cnt = q.popleft()
        if cnt == K:
            if ans < num:
                ans = num
        else:
            for i in range(size):
                iDigit = size - i
                inum = num % (10 ** iDigit) // (10 ** (iDigit - 1))
                for j in range(i + 1, size):
                    jDigit = size - j
                    jnum = num % (10 ** jDigit) // (10 ** (jDigit - 1))
                    if i == 0 and jnum == 0:
                        continue
                    newNum = num - (jnum * (10 ** (jDigit - 1))) - (inum * (10 ** (iDigit - 1)))
                    newNum += (inum * (10 ** (jDigit - 1))) + (jnum * (10 ** (iDigit - 1)))
                    if visited[newNum] >= cnt:
                        continue
                    visited[newNum] = cnt
                    q.append((newNum, cnt + 1))
    return ans
    
def solve():
    N, K = input().split()
    if len(N) == 1 or (len(N) == 2 and N[1] == "0"):
        return -1
    return bfs(int(N), int(K), len(N))

print(solve())