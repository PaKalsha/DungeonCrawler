from actors import Actor

class Monster(Actor):
    count = {
        'undead': 0,
        'beast': 0,
        'dragon': 0
    }
    
    @classmethod  # does not rely on instance data; returns data about the class
    def get_count(cls):
        return cls.count

class Undead(Actor):
    def die(self):
        Monster.count['undead'] += 1
        super(Undead, self).die()

class SkelWar(Undead):
    def __init__(self):
        self.name = "Skeleton Warrior"
        self.maxHP = 30
        self.maxMP = 5
        self.special = {
            "STR": 6,
            "PER": 4,
            "END": 6,
            "CHA": 0,
            "INT": 3,
            "AGL": 6,
            "LUCK": 3
        }
        super(SkelWar, self).__init__(
            name = self.name,
            maxHP = self.maxHP,
            maxMP = self.maxMP,
            special = self.special
        )
        self.equipment = ['horned__helm']
        self.inventory = ['50 gold']

class Zombie(Undead):
    def __init__(self):
        self.name = "Zombie"
        self.maxHP = 15
        self.maxMP = 0
        self.special = {
            "STR": 4,
            "PER": 2,
            "END": 5,
            "CHA": 0,
            "INT": 2,
            "AGL": 1,
            "LUCK": 5
        }
        super(Zombie, self).__init__(
            name = self.name,
            maxHP = self.maxHP,
            maxMP = self.maxMP,
            special = self.special
        )
        self.inventory = None

## ---------------------------

class Beast(Actor):
    def die(self):
        Monster.count['beast'] += 1
        super(Beast, self).die()

class Hellhound(Beast):
    pass

## ---------------------------

class Dragon(Actor):
    def die(self):
        Monster.count['dragon'] += 1
        super(Dragon, self).die()

class Drake(Dragon):
    def __init__(self):
        self.name = "Drake"
        self.maxHP = 40
        self.maxMP = 120
        self.special = {
            "STR": 3,
            "PER": 6,
            "END": 4,
            "CHA": 7,
            "INT": 8,
            "AGL": 8,
            "LUCK": 5
        }
        super(Drake, self).__init__(
            name = self.name,
            maxHP = self.maxHP,
            maxMP = self.maxMP,
            special = self.special
        )

class Wyvern(Dragon):
    pass

if __name__ == '__main__':
    skel = SkelWar()
    zom = Zombie()
    print zom
    print zom.print_stats()
    zom.die()
    skel.die()
    print Monster.count
