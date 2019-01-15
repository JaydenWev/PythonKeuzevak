# opties in het veld
blank = '░░░'
# blank = '▓▓▓'
leeg = '   '
zwart = ' b '
zwartK = '=B='
wit = ' w '
witK = '=W='

# rijen van het veld
een     = [blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, ' 1']
twee    = [zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, ' 2']
drie    = [blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, ' 3']
vier    = [zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, ' 4']
vijf    = [blank, leeg, blank, leeg, blank, leeg, blank, leeg, blank, leeg, ' 5']
zes     = [leeg, blank, leeg, blank, leeg, blank, leeg, blank, leeg, blank, ' 6']
zeven   = [blank, wit, blank, wit, blank, wit, blank, wit, blank, wit, ' 7']
acht    = [wit, blank, wit, blank, wit, blank, wit, blank, wit, blank, ' 8']
negen   = [blank, wit, blank, wit, blank, wit, blank, wit, blank, wit, ' 9']
tien    = [wit, blank, wit, blank, wit, blank, wit, blank, wit, blank, ' 10']
elf     = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ']

veld            = ['']
veldString      = ['']

def setBeginVeld():
    global een
    global twee
    global drie
    global vier
    global vijf
    global zes
    global zeven
    global acht
    global negen
    global tien
    global elf
    # alles op begin positie zetten
    een     = [blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, ' 1']
    twee    = [zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, ' 2']
    drie    = [blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, ' 3']
    vier    = [zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, ' 4']
    vijf    = [blank, leeg, blank, leeg, blank, leeg, blank, leeg, blank, leeg, ' 5']
    zes     = [leeg, blank, leeg, blank, leeg, blank, leeg, blank, leeg, blank, ' 6']
    zeven   = [blank, wit, blank, wit, blank, wit, blank, wit, blank, wit, ' 7']
    acht    = [wit, blank, wit, blank, wit, blank, wit, blank, wit, blank, ' 8']
    negen   = [blank, wit, blank, wit, blank, wit, blank, wit, blank, wit, ' 9']
    tien    = [wit, blank, wit, blank, wit, blank, wit, blank, wit, blank, ' 10']
    elf     = [' 1|', '|2|', '|3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10 ']
    toString()

def toString():
    global veld
    global veldString

    veld = [een, twee, drie, vier, vijf, zes, zeven, acht, negen, tien, elf]
    # omzetten naar string
    rijEen = ''.join(een)
    rijTwee = ''.join(twee)
    rijDrie = ''.join(drie)
    rijVier = ''.join(vier)
    rijVijf = ''.join(vijf)
    rijZes = ''.join(zes)
    rijZeven = ''.join(zeven)
    rijAcht = ''.join(acht)
    rijNegen = ''.join(negen)
    rijTien = ''.join(tien)
    rijElf = ''.join(elf)
    veldString = [rijEen, rijTwee, rijDrie, rijVier, rijVijf, rijZes, rijZeven, rijAcht, rijNegen, rijTien, rijElf]
    # printen
    for i in range (0, 11):
        print(veldString[i])