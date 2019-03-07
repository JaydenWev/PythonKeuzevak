from Player import player

import Field as f
import Select as s

selectedRow = 0
selectedColumn = 0

sp1 = player(1)
sp2 = player(2)

def play():
    f.setBeginField()
    s.selecteerStap()


def selectMove(player):
    selected = s.selectPos()
    selectedRow = selected[0]
    selectedColumn = selected[1]
    damPos = f.veld[selectedRow][selectedColumn]


play()
# selectMove(sp1)