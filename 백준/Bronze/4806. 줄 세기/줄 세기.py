i = 0
while 1:
    try:
        input()
        i += 1
    except EOFError:
        break
print(i)