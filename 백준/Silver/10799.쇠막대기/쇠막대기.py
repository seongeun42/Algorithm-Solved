#10799

from sys import stdin

#express laser as '/'
expression = stdin.readline().rstrip().replace("()","/")

stack = 0
result = 0
for char in expression:
  if char == '(':
    stack += 1
  elif char == ')':
    stack -= 1
    result += 1
  else: #if char == '/' (laser)
    result += stack

print(result)