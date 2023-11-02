s = []
while 1:
    try:
        s.append(input())
    except:
        break
s = "".join(s)
print(sum(map(int, s.split(","))))