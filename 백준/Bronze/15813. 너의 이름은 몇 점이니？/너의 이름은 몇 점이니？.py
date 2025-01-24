L = int(input())
name = input()
ans = sum([ord(c) for c in name])
print(ans - (ord('A') - 1) * L)