N = int(input())
chains = sorted([*map(int, input().split())])
cnt = N
connected = 1
for c in chains:
    if connected + c >= cnt:
        break
    else:
        connected += c
        cnt -= 1
print(cnt - 1)