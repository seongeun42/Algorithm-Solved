import sys
input = sys.stdin.readline

def solve():
    K, L = map(int, input().split())
    wait_list = {}
    for i in range(L):
        num = input().rstrip()
        if num in wait_list:
            cnt = wait_list[num][0]
            wait_list[num] = (cnt + 1, i)
        wait_list[num] = (1, i)
    wait_list = sorted(wait_list.items(), key=lambda x: (x[1][0], x[1][1]))
    for i in range(min(K, len(wait_list))):
        print(wait_list[i][0])

solve()