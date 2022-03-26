N = int(input())
exe = input()
num = [int(input()) for _ in range(N)]
op = {'+', '-', '*', '/'}
s = []
A = ord('A')
for v in exe:
    if v in op:
        o2, o1 = s.pop(), s.pop()
        if v == '+':
            s.append(o1 + o2)
        elif v == '-':
            s.append(o1 - o2)
        elif v == '*':
            s.append(o1 * o2)
        else:
            s.append(o1 / o2)
    else:
        s.append(num[ord(v) - A])
print(f'{s[0]:.2f}')