roman = { 'M': 1000, 'CM': 900, 'D': 500,
    'CD': 400, 'C': 100, 'XC': 90,
    'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
    'V': 5, 'IV': 4, 'I': 1 }

def romanToInt(s):
    num = 0
    prev = 0
    for v in s[::-1]:
        num += -roman[v] if roman[v] < prev else roman[v]
        prev = roman[v]
    return num

def intToRoman(n):
    s = ''
    for k, v in roman.items():
        cnt, n = divmod(n, v)
        s += k * cnt
    return s

n = romanToInt(input()) + romanToInt(input())
print(n, intToRoman(n), sep='\n')