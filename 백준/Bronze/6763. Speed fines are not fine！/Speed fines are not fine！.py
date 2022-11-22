calc = int(input()) - int(input())
res = 0
if -20 <= calc < 0:
    res = 100
elif -30 <= calc < -20:
    res = 270
elif calc < -30:
    res = 500
if res == 0:
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is $", res, ".", sep="")