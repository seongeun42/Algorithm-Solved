menu = [int(input()) for _ in range(5)]
print(min(menu[:3]) + min(menu[3:]) - 50)