from player import player
from field import field


f = field()

sp1 = player(True)
sp2 = player(False)

def play():
    print(f.blank)
    f.setBeginField()
    f.hoi()

play()