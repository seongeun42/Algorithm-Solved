t = int(input())
for i in range(t):
    input()
    N, M = map(int, input().split())
    sj = sorted([*map(int, input().split())], reverse=True)
    sb = sorted([*map(int, input().split())], reverse=True)
    while sj and sb:
        sb.pop() if sj[-1] >= sb[-1] else sj.pop()
    if sj:
        print('S')
    elif sb:
        print('B')
    else:
        print('C')