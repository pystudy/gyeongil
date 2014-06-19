class Unit:
	hp=100
	hpMax=100
	STR=25
	DEF=20

	name = ""

	def __init__(self, name):
		self.name = name

	def status(self):
		print("%3d/%3d" % (self.hp, self.hpMax))

	def attack(self, unit):
		damage = self.STR - unit.DEF/2
		unit.hp -= damage

		return "%s의 공격!\n%s은 %s에게 %d의 피해를 입혔다!" % (self.name,self.name, unit.name, damage)
	
	def isAlive(self):
		if self.hp < 0: 
			return "false";
		return "true";

class Battle:

	now = "now"
	finish = "finish"	

	def fight(self,attacker, defender):
		print(attacker.attack(defender))
		return attacker

	def turn(self, foo, bar):
		self.fight(foo, bar)
		if bar.isAlive() == "true":
			self.fight(bar, foo)
			if foo.isAlive() == "false":
				print("%s가 %s를 쓰러뜨렸다" % (bar.name, foo.name))
		else:
			print("%s가 %s를 쓰러뜨렸다!" % (foo.name, bar.name))
			return self.finish
	
foo = Unit("코니")
foo2 = Unit("브라운")
control = Battle()

while control.turn(foo, foo2) != control.finish:
	pass


