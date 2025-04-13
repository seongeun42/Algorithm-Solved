X = input()
ans = int(X) + 1
ordered = ''.join(sorted(list(X)))
while 1:
    tmp = ''.join(sorted(list(str(ans))))
    if len(ordered) < len(tmp):
        print(0)
        break
    if ordered == tmp:
        print(ans)
        break
    ans += 1