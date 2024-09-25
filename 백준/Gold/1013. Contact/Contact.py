import sys
input = sys.stdin.readline

def check(cur, string):
    cnt = 0
    if cur < len(string) and string[cur] == '0':
        cnt += 1
    while cur < len(string) and string[cur] == '0':
        cur += 1
    if cur < len(string) and string[cur] == '1':
        cnt += 1
    while cur < len(string) and string[cur] == '1':
        cur += 1
    return cur if cnt == 2 else -1
    
def dfs(cur, string):
    if cur >= len(string):
        return True
    if string[cur:cur+2] == "01":
        if dfs(cur + 2, string):
            return True
    if string[cur:cur+2] == "10":
        nxt = check(cur + 2, string)
        if nxt >= 0:
            if dfs(nxt, string):
                return True
            if string[nxt - 2] == '1' and dfs(nxt - 1, string):
                return True
    return False

def solve():
    T = int(input())
    for _ in range(T):
        string = input().rstrip()
        print("YES" if dfs(0, string) else "NO")

solve()