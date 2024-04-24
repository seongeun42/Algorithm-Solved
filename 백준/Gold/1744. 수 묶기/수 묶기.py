import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([int(input()) for _ in range(N)])
neg = [v for v in nums if v <= 0][::-1]
pos = [v for v in nums if v > 0]
ans = 0
while len(neg) > 1:
    ans += neg.pop() * neg.pop()
while len(pos) > 1:
    a, b = pos.pop(), pos.pop()
    ans += max(a * b, a + b)
if neg and pos:
    ans += max(neg[0] * pos[0], neg[0] + pos[0])
elif neg:
    ans += neg[0]
elif pos:
    ans += pos[0]
print(ans)