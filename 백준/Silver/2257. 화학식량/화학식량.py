s = list(input()[::-1])
weight = {'H': 1, 'C': 12, 'O': 16}
stack = []
while s:
    c = s.pop()
    if c == '(':
        stack.append(c)
    elif c == ')':
        tmp = 0
        while stack[-1] != '(':
            tmp += stack.pop()
        stack.pop()
        stack.append(tmp)
    elif c.isdecimal():
        stack.append(stack.pop() * int(c))
    else:
        stack.append(weight[c])
print(sum(stack))