def toCpp():
    if A <= ord(s[0]) <= Z:
        return "Error!"
    ans = ""
    for c in s:
        if A <= ord(c) <= Z:
            ans += "_" + c.lower()
        else:
            ans += c
    return ans

def toJava():
    if s[0] == '_' or s[-1] == '_' or "__" in s:
        return "Error!"
    ans = ""
    pre = 0
    for c in s:
        if A <= ord(c) <= Z:
            return "Error!"
        if c != '_':
            if pre == '_':
                ans += c.upper()
            else:
                ans += c
        pre = c
    return ans

s = input()
flag = 0
A, Z = ord('A'), ord('Z')
if '_' in s:
    print(toJava())
else:
    print(toCpp())