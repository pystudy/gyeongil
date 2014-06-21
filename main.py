from model.Unit import Unit
from Dao.Battle import Battle

foo = Unit("코니")
bar = Unit("브라운")

control = Battle()

while (control.turn(foo, bar)) != control.finish:
    pass
