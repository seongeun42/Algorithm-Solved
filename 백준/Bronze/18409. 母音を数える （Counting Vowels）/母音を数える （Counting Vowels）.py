n = int(input())
s = input()
mo = "aiueo"
print(sum([s.count(mo[i]) for i in range(5)]))