import extra as ext

def getalSelecteren(var):
    invoer = input('kies uw '+ var + ':')
    if 'q' in invoer:
        ext.shutdown()
    Num = True
    while Num:
        if (invoer != '1') and invoer != '2'and invoer != '3' and invoer != '4' and invoer != '5' and invoer != '6' and invoer != '7' and invoer != '8' and invoer != '9' and invoer != '10':
            invoer = input("\n"
                              "dat is geen geldig getal. "
                              "\n"
                              "kies uw rij: ")
        else:
            Num = False
    return int(invoer)

def selecteerDam():
    rij = getalSelecteren('rij')
    kolom = getalSelecteren('kolom')
    dam = [rij, kolom]
    return dam

