i = 0
for a in open('512_server-IndiaSpeaks-comment.json').read().splitlines():
    i += 1
    print(i, end='\r')
    #a1 = a.replace('\'', '')
    open('mix.json', 'a+').write(a + '\n')
