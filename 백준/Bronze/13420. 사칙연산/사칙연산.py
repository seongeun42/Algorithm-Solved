T = int(input())
for _ in range(T):
    s = input().split()
    num = 0
    if s[1] == '+':
        num = int(s[0]) + int(s[2])
    elif s[1] == '-':
        num = int(s[0]) - int(s[2])
    elif s[1] == '*':
        num = int(s[0]) * int(s[2])
    elif s[1] == '/':
        num = int(s[0]) // int(s[2])
    print("correct" if num == int(s[-1]) else "wrong answer")