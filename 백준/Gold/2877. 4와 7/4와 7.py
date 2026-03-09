K = int(input())
two = [1]
total = 0
while total + two[-1] * 2 < K:
    two.append(two[-1] * 2)
    total += two[-1]
ans = ""
for c in bin(K - total - 1)[2:]:
    ans += '4' if c == '0' else '7'
ans = '4' * (len(two) - len(ans)) + ans
print(ans)