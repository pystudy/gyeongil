__author__ = 'yuinacor'


class Battle:
    now = "now"
    finish = "finish"

    def fight(self, attacker, defender):
        print(attacker.attack(defender))
        return attacker

    def print_log(self, logs):
        split_log = []
        merged_log = []
        for i in logs:
            split_log.append(i.split("\n"))

        for i in range(0, len(split_log[0])):
            line = ""
            for j in range(0, len(split_log)):
                line += split_log[j][i]
                line += "\t"
            merged_log.append(line)
        for i in merged_log:
            print(i)

    def turn(self, foo, bar):
        self.fight(foo, bar)
        if bar.isAlive() == "true":
            self.fight(bar, foo)
            if foo.isAlive() == "false":
                print("%s가 %s를 쓰러뜨렸다" % (bar.name, foo.name))
                return self.finish
        else:
            print("%s가 %s를 쓰러뜨렸다!" % (foo.name, bar.name))
            return self.finish
        self.print_log([foo.status(), bar.status()])