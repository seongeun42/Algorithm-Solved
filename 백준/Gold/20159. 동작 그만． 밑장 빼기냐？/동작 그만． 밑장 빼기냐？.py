N = int(input())
card = [*map(int, input().split())]
odd = [0, card[0]]
even = [0]
for i in range(2, N, 2):
    odd.append(odd[-1] + card[i])
    even.append(even[-1] + card[N - i - 1])
even = even[::-1]
ans = 0
for i in range(N // 2):
    ans = max(ans, odd[i] + card[-1] + even[i])
    ans = max(ans, odd[i + 1] + even[i])
print(ans)