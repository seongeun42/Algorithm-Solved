ans = -1

def backtrack(dep, N, K, size, visited):
    num = int("".join(N))
    if num in visited[dep]:
        return
    visited[dep].add(num)
    global ans
    if dep == K:
        res = num
        if ans < res:
            ans = res
        return
    for i in range(size):
        for j in range(i + 1, size):
            if i == 0 and N[j] == "0":
                continue
            N[i], N[j] = N[j], N[i]
            backtrack(dep + 1, N, K, size, visited)
            N[i], N[j] = N[j], N[i]
    
def solve():
    N, K = input().split()
    if len(N) == 1 or (len(N) == 2 and N[1] == "0"):
        print(-1)
    else:
        visited = [set() for _ in range(int(K) + 1)]
        backtrack(0, list(N), int(K), len(N), visited)
        print(ans)

solve()