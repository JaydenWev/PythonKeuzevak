# houdt de hoeveelheid beurten zijn geweest
beurtCounter = 1
# welke speler is aan zet
activeSpeler = 'w'
# houdt bij hoeveel stenen de speler nog heeft
dammenW = 20
dammenB = 20

def wisselSpeler():
    global activeSpeler
    global beurtCounter

    if activeSpeler =='w':
        activeSpeler = 'b'
    if activeSpeler =='b':
        activeSpeler = 'w'
        beurtCounter += 1