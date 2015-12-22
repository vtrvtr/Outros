import livestreamer


stream = livestreamer.streams('http://twitch.tv/beyondthesummit')
stream2 = livestreamer.streams('http://twitch.tv/lmao')


if not stream2:
    print('lol')

