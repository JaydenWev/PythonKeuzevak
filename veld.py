

# blank = "░"
blank = "▓"
leeg = "  "
zwart = "b "
wit = "w "

# rijen van het veld
een     = [blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart]
twee    = [zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank]
drie    = [blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart]
vier    = [zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank]
vijf    = [blank, leeg, blank, leeg, blank, leeg, blank, leeg, blank, leeg]
zes     = [leeg, blank, leeg, blank, leeg, blank, leeg, blank, leeg, blank]
zeven   = [blank, wit, blank, wit, blank, wit, blank, wit, blank, wit]
acht    = [wit, blank, wit, blank, wit, blank, wit, blank, wit, blank]
negen   = [blank, wit, blank, wit, blank, wit, blank, wit, blank, wit]
tien    = [wit, blank, wit, blank, wit, blank, wit, blank, wit, blank]

def setBeginVeld():
    een     = [blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart]
    twee    = [zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank]
    drie    = [blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart]
    vier    = [zwart, blank, zwart, blank, zwart, blank, zwart, blank, zwart, blank]
    vijf    = [blank, leeg, blank, leeg, blank, leeg, blank, leeg, blank, leeg]
    zes     = [leeg, blank, leeg, blank, leeg, blank, leeg, blank, leeg, blank]
    zeven   = [blank, wit, blank, wit, blank, wit, blank, wit, blank, wit]
    acht    = [wit, blank, wit, blank, wit, blank, wit, blank, wit, blank]
    negen   = [blank, wit, blank, wit, blank, wit, blank, wit, blank, wit]
    tien    = [wit, blank, wit, blank, wit, blank, wit, blank, wit, blank]


def toString():
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

    print(rijEen)
    print(rijTwee)
    print(rijDrie)
    print(rijVier)
    print(rijVijf)
    print(rijZes)
    print(rijZeven)
    print(rijAcht)
    print(rijNegen)
    print(rijTien)
