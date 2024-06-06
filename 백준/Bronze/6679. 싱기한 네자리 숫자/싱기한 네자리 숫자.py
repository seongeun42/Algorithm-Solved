def convert(num, base):
    if num == 0:
        return 0
    return num % base + convert(num // base, base)
        
for v in range(1000, 10000):
    if convert(v, 10) == convert(v, 12) == convert(v, 16):
        print(v)