n, p = map(int, input().split())
ans = [n]
num = n
while 1:
    num = num * n % p
    if num not in ans:
        ans.append(num)
    else:
        ans = ans[ans.index(num):]
        break
print(len(ans))