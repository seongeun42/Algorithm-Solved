import re
n = int(input())
print(sum(map(int, re.sub(r'[a-zA-Z]', ' ', input()).split())))