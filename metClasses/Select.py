import Extra as ext

def selectNum(var):
    playerInput = input('select your' + var)
    if 'q' in playerInput:
        ext.shutdown()
    Num = True
    while Num:
        if (playerInput != '1') and playerInput != '2' and playerInput != '3' and playerInput != '4' and playerInput != '5' and playerInput != '6' and playerInput != '7' and playerInput != '8' and playerInput != '9' and playerInput != '10':
            playerInput = input("\n"
                           "dat is geen geldig getal. "
                           "\n"
                           "kies uw " + var + ": ")
        else:
            playerInput = int(playerInput) - 1
            Num = False
    return int(playerInput)

def selectPos():
    row = selectNum('row')
    column = selectNum('column')
    damPos = [row, column]
    return damPos


