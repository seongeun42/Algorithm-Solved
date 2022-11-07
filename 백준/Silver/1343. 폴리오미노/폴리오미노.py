b = input()
b = b.replace("XXXX", "AAAA")
b = b.replace("XX", "BB")
print(b if 'X' not in b else -1)