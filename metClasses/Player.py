class player:
    playerSymbol = ''
    # houdt bij hoeveel stenen de speler nog heeft
    damAmount = 20

    def __init__(self, playerNum):       # constructor
        if playerNum == 1:
            playerSymbol = 'w'
        elif playerNum == 2:
            playerSymbol = 'b'






    # geeft aan of er een winnaar is
    isWinner = False
    # houdt de hoeveelheid beurten zijn geweest
    beurtCounter = 1
    # welke speler is aan zet
    activeSpeler = 'w'
    inActiveSpeler = 'b'

    def wisselSpeler():
        global activeSpeler
        global beurtCounter

        if activeSpeler =='w':
            activeSpeler = 'b'
        if activeSpeler =='b':
            activeSpeler = 'w'
            beurtCounter += 1

