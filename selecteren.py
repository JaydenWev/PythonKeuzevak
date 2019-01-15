import extra as ext
import veld as v

def positieSelecteren(var):
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
            invoer = int(invoer) - 1
            Num = False
    return int(invoer)

def selecteerDam():
    rij = positieSelecteren('rij')
    kolom = positieSelecteren('kolom')
    damPositie = [rij, kolom]
    return damPositie

def selecteerStap():
    select = selecteerDam()
    rij = select[0]
    kolom = select[1]

    # print(v.veld[rij])