input = __import__('sys').stdin.readline

gw = 0

N = int(input().strip())
for _ in range(int(N)):
    string = str(input().strip())
    
    while(string.count("AA") > 0 or string.count("BB") > 0):
        string = string.replace("AA","").replace("BB","")

    if(string == ""):
        gw += 1

print(gw)