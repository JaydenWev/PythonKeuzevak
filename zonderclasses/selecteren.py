import extra as ext
import veld as v
import speler as sp

def selecteerNum(var):
    invoer = input('speler \'' + sp.activeSpeler + '\' kies uw '+ var + ':')
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

def positieSelecteren():
    rij = selecteerNum('rij')
    kolom = selecteerNum('kolom')
    damPositie = [rij, kolom]
    return damPositie

def selecteerStap():
    select = positieSelecteren()
    # geselecteerde dam
    rij = select[0]
    kolom = select[1]
    dam = v.veld[rij][kolom]
    # print(v.veld[rij])
    # print('\'', dam, '\'')

# welke dam is het (kleur en koning)
    # de juiste kleur dam is gekozen
    if sp.activeSpeler in dam:
        if '=' in dam:
            print("dat is jouw koning!")
        else:
            print("Dat is jouw dam")
    # Er is een leeg vak gekozen
    elif sp.activeSpeler not in dam:
       print('Dat is geen dam!')
    # verkeerde kleur dam is gekozen
    elif v.blank in dam:
        print('Dat is niet jouw dam!')
#        if sp.activeSpeler =='w':
    # moet je slaan/eten

    # wilt naar
    doel = positieSelecteren()
    rijDoel = select[0]
    kolomDoel = select[1]
    #als succesvol
    sp.wisselSpeler()