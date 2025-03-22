bowie = [
(1967, 'DavidBowie'),
(1969, 'SpaceOddity'),
(1970, 'TheManWhoSoldTheWorld'),
(1971, 'HunkyDory'),
(1972, 'TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'),
(1973, 'AladdinSane'),
(1973, 'PinUps'),
(1974, 'DiamondDogs'),
(1975, 'YoungAmericans'),
(1976, 'StationToStation'),
(1977, 'Low'),
(1977, 'Heroes'),
(1979, 'Lodger'),
(1980, 'ScaryMonstersAndSuperCreeps'),
(1983, 'LetsDance'),
(1984, 'Tonight'),
(1987, 'NeverLetMeDown'),
(1993, 'BlackTieWhiteNoise'),
(1995, '1.Outside'),
(1997, 'Earthling'),
(1999, 'Hours'),
(2002, 'Heathen'),
(2003, 'Reality'),
(2013, 'TheNextDay'),
(2016, 'BlackStar')
]
for _ in range(int(input())):
    n, m = map(int, input().split())
    if n < 1967:
        n = 1967
    album = []
    for i in range(n, m+1):
        for b in bowie:
            if b[0] == i:
                album.append(b)
    print(len(album))
    if album:
        [print(*a) for a in album]