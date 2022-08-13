small = "abcdefghijklmnopqrstuvwxyz"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
for c in s:
    if c.islower():
        print(small[(ord(c) - ord('a') + 13) % 26], end='')
    elif c.isupper():
        print(big[(ord(c) - ord('A') + 13) % 26], end='')
    else:
        print(c, end='')