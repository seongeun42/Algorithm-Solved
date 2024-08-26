sosu = [0] + [1, 0] * 550
sosu[2] = 1
for i in range(3, int(1100 ** 0.5)):
    if sosu[i] == 1:
        for j in range(i + i, 1100, i):
            sosu[j] = 0
hap = 0
word = input()
for c in word:
    hap += ord(c) - 96 if c.islower() else ord(c) - 38
print(f"It is {'' if sosu[hap] else 'not '}a prime word.")