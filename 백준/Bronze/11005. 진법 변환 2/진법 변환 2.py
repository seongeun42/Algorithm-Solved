n, b = map(int, input().split())
A = ord("A") - 10
ans = ""
while n:
    n, m = divmod(n, b)
    if m < 10:
        ans += str(m)
    else:
        ans += chr(A + m)
print(ans[::-1])