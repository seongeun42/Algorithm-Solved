from collections import deque

def bfs(N, K, size):
    q = {(N, 0)}
    ans = -1
    while q:
        num, cnt = q.pop()
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
                    q.add((newNum, cnt + 1))
    return ans
    
def solve():
    N, K = input().split()
    print(bfs(int(N), int(K), len(N)))

solve()