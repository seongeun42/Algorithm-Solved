s = input()
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for c in s:
    print(a[ord(c) - ord('A') - 3], end="")