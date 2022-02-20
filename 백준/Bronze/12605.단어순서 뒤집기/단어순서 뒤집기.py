N = int(input())
for i in range(1, N+1):
    line = input().split()
    print("Case #" + str(i) + ":", *line[::-1])