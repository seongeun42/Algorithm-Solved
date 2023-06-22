spb = {1996, 1997, 2000, 2007, 2008, 2013, 2018}
y = int(input())
if y == 2006:
    print("PetrSU, ITMO")
else:
    print("SPbSU" if y in spb else "ITMO")