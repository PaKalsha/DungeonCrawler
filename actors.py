
import abc
# research abc module (abstract base class)

class Actor(object):
    """
    Represents all monsters, merchants, companions and the player character
    """
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, name, maxHP, maxMP, special):
        self.name = name
        self.maxHP = maxHP
        self.currHP = self.maxHP       # Initial health is at maximum
        self.maxMP = maxMP
        self.currMP = self.maxHP       # Initial MP is at maximum
        self.status = {
            'dead': False,
            'poisoned': False,
            'cursed': False,
            'silenced': False
        }

        ## Physical traits
        self.special = special
        self.buffs = {
                    "STR": 0,     # STR affects physical damage
                    "PER": 0,     # PER affects critical chance
                    "END": 0,     # END affects physical defence
                    "CHA": 0,     # CHA affects magic damage
                    "INT": 0,     # INT affects magic defence
                    "AGL": 0,     # AGL affects evade chance
                    "LUCK": 0     # LUCK affects enemy encounter frequency
        }
        self.attack = self.special['STR'] + self.buffs['STR']
        self.defence = self.special['END'] + self.buffs['END']
        self.wisdom = self.special['INT'] + self.buffs['INT']

        self.equipment = None
        self.inventory = None

    def __str__(self):
        return "The {} is {}".format(self.name, self.get_status())

    def is_alive(self):
        """
        True if not dead
        """
        return not self.status['dead']

    def get_name(self):
        """
        Return actor's name
        """
        return self.name

    def get_health(self):
        """
        Return a tuple: current health/max health
        """
        return self.maxHP, self.currHP

    def get_status(self):
        """
        Return a general description of the actor's health
        """
        if self.currHP / float(self.maxHP) == 1.0:
            state = "unharmed"
        elif self.currHP / float(self.maxHP) > 0.80:
            state = "slightly hurt"
        elif self.currHP / float(self.maxHP) > 0.50:
            state = "visibly injured"
        elif self.currHP / float(self.maxHP) > 0.15:
            state = "badly wounded"
        elif self.currHP / float(self.maxHP) > 0.00:
            state = "near death"
        else:
            return "dead"

        for key in self.status:
            if self.status[key] is True:
                state += " and {}".format(key)
        return state

    def get_stats(self):
        """
        Return the stats and buffs
        """
        ## TODO: Return buffs
        return self.special

    def get_attack_power(self):
        """
        Returns the actor's attack power
        """
        return self.attack

    def get_defense(self):
        """
        Returns the actor's defensive capability
        """
        return self.defence

    def get_wisdom(self):
        """
        Returns the actor's wisdom rating
        """
        return self.wisdom

    def print_stats(self):
        """
        Return the actor's stats
        """
        stats = "STR: " + str(self.special["STR"]) + "\r\n" + \
                "PER: " + str(self.special["PER"]) + "\r\n" + \
                "END: " + str(self.special["END"]) + "\r\n" + \
                "CHA: " + str(self.special["CHA"]) + "\r\n" + \
                "INT: " + str(self.special["INT"]) + "\r\n" + \
                "AGL: " + str(self.special["AGL"]) + "\r\n" + \
                "LUCK: " + str(self.special["LUCK"])
        return stats

    def take_damage(self, damage):
        """
        Reduce the actor's current health
        """
        self.currHP -= damage
        if self.currHP < 1:
            self.die()

    def heal(self, amount):
        """
        Actor regains health
        """
        self.currHP += amount
        if self.currHP > self.maxHP:
            self.currHP = self.maxHP

    def buff(self, stat, amount, duration):
        """
        Actor increases a given stat
        """
        self.buffs[stat] += amount

    def die(self):
        """
        Set Actor death state
        """
        self.status['dead'] = True

    def poisoned(self):
        """
        Actor becomes poisoned
        """
        self.status['poisoned'] = True

    def cursed(self):
        """
        Actor becomes cursed
        """
        self.status['cursed'] = True

    def silenced(self):
        """
        Actor becomes unable to use magic
        """
        self.status['silenced'] = True


if __name__ == '__main__':
    player = Actor(
        name = 'Player',
        maxHP = 100,
        maxMP = 100,
        special = {
            'STR': 7,
            'PER': 7,
            'END': 7,
            'CHA': 7,
            'INT': 7,
            'AGL': 7,
            'LUCK': 7
        }
    )
    player.cursed()
    player.silenced()
    print player
