N = int(input())
scoville = sorted([*map(int, input().split())])
prefix = [scoville[0]]
for i in range(1, N):
    prefix.append(prefix[i - 1] + scoville[i])
total = 0
for i in range(N - 1):
    diff = prefix[-1] - prefix[i] - prefix[N - i - 2]
    total += (diff * (2 ** i)) % 1_000_000_007
print(total % 1_000_000_007)