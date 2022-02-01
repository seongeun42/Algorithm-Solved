s = input()
print(*sorted([s[i:len(s)] for i in range(len(s))]), sep='\n')