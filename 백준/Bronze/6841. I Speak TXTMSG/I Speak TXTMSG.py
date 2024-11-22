import sys
input = sys.stdin.readline

def solve():
    stat = {"CU": "see you", ":-)": "I’m happy", ":-(": "I’m unhappy",
            ";-)": "wink", ":-P": "stick out my tongue", "(~.~)": "sleepy",
            "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "because",
            "TY": "thank-you", "YW": "you’re welcome"}
    while 1:
        s = input().strip()
        if s == "TTYL":
            print("talk to you later")
            return
        print(stat.get(s, s))
    
solve()