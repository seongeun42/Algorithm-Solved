while 1:
    x, y = map(float, input().split())
    if x == 0 or y == 0:
        print("AXIS")
    elif x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif x > 0 and y < 0:
        print("Q4")
    if x == 0 and y == 0:
        break