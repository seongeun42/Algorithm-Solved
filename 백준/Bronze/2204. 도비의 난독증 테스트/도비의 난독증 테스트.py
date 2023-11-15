while 1:
    n = int(input())
    if n == 0:
        break
    words = [input() for _ in range(n)]
    sortedWords = sorted([[words[i].lower(), i] for i in range(n)])
    print(words[sortedWords[0][1]])