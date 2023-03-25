s = input()
hap = s.count(":-)")
sad = s.count(":-(")
if hap + sad == 0:
    print("none")
elif hap == sad:
    print("unsure")
elif hap > sad:
    print("happy")
else:
    print("sad")