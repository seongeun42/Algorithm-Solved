for _ in range(int(input())):
    N, K = map(int, input().split())
    candy = [*map(int, input().split())]
    ans = sum([v // K for v in candy])
    print(ans)