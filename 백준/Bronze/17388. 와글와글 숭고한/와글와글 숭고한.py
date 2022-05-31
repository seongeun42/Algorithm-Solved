S, K, H = map(int, input().split())
if S + K + H >= 100:
    print("OK")
else:
    v = min(S, K, H)
    if v == S:
        print("Soongsil")
    elif v == K:
        print("Korea")
    else:
        print("Hanyang")