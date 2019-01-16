import veld as v            # importeer veld functies
import selecteren as sel    # importeer selecteer functies
import speler as sp

def spelen():
    v.setBeginVeld()
    while not sp.isWinner:
        sel.selecteerStap()

spelen()

