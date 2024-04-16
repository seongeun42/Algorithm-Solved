import sys
input = sys.stdin.readline

cnt = 10
ans = []

def backtrack(dep, max_dep, idx, list, N):
    global cnt, ans
    n = "0123456789"
    if dep == max_dep:
        cnt += 1
        ans.append(int("".join(list)[::-1]))
        return
    for i in range(idx, 10):
        list.append(n[i])
        backtrack(dep + 1, max_dep, i + 1, list, N)
        list.pop()

def solve():
    N = int(input()) - 1
    n = "0123456789"
    if N < 10:
        return n[N]
    for i in range(2, 11):
        backtrack(0, i, 0, [], N)
    return sorted(ans)[N - 10] if N - 10 < len(ans) else -1
    
print(solve())