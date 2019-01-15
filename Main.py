import veld as v            # importeer veld functies
import selecteren as sel    # importeer selecteer functies

v.setBeginVeld()

sel.selecteerStap()

def spelen():
    v.setBeginVeld()
    while isNoWinner:
        sel.selecteerStap()