import random


class Unit:
    hp = 100
    hpMax = 100
    STR = 25
    DEF = 20

    name = ""

    def __init__(self, name):
        self.name = name

    def status(self):
        result = "\n"
        result += "%s의 스테이터스\n" % (self.name)
        result += "=" * 12
        result += "\n"
        result += "hp : %3d/%3d\n" % (self.hp, self.hpMax)
        result += "=" * 12
        result += "\n"

        return result

    def attack(self, unit):
        damage = self.STR * random.randint(5, 15) / 10 - self.DEF

        if damage < 0:
            damage = 0

        if damage > unit.hp:
            unit.hp = 0
        else:
            unit.hp -= damage

        return "%s의 공격!\n%s은 %s에게 %d의 피해를 입혔다!" % (self.name, self.name, unit.name, damage)

    def isAlive(self):
        if (self.hp <= 0):
            return "false"
        return "true"
