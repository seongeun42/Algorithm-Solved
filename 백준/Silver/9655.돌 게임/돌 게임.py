n = int(input())
th, on = divmod(n, 3)
print('SK' if (th + on) % 2 else 'CY')