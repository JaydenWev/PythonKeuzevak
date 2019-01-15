def selecteerRij():
    selecteerRij = input('kies uw rij: ')
    rijInt = True
    while rijInt:
        print('\'' + selecteerRij + '\'')
        if (selecteerRij != '1') and selecteerRij != '2'and selecteerRij != '3' and selecteerRij != '4' and selecteerRij != '5' and selecteerRij != '6' and selecteerRij != '7' and selecteerRij != '8' and selecteerRij != '9' and selecteerRij != '10':
            selecteerRij = input("\n"
                              "dat is geen geldig getal. "
                              "\n"
                              "kies uw rij: ")
        else:
            rijInt = False
    return int(selecteerRij)



def selecteerKolom():
    selecteerKolom = input('kies uw kolom: ')
    kolomInt = True
    while kolomInt:
        print('\'' + selecteerKolom + '\'')
        if (selecteerKolom != '1') and selecteerKolom != '2'and selecteerKolom != '3' and selecteerKolom != '4' and selecteerKolom != '5' and selecteerKolom != '6' and selecteerKolom != '7' and selecteerKolom != '8' and selecteerKolom != '9' and selecteerKolom != '10':
            selecteerKolom = input("\n"
                              "dat is geen geldig getal. "
                              "\n"
                              "kies uw kolom: ")
        else:
            kolomInt = False
    return int(selecteerKolom)
