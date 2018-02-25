import random

from actors import Actor
from monsters import Monster


def create_character(self):
    """
    Offer player a chance to re-roll their character's stats
    """
    pass


class PlayerCharacter(Actor):
    """
    Player character only
    """
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def get_score():
        return Monster.get_count()

    def get_inv(self):
        """
        Return items in the inventory and their quantity
        """
        return self.inventory

    def has_item(self, item):
        """
        Check the player has a given item
        """
        if item in self.inventory:
            return True
        else:
            return False

    def get_player_status(self):
        """
        Return a detailed report of the player status
        """
        pass

    def equip_item(self, equipment, equipment_type):
        """
        Equip an item
        """
        if self.has_item:
            pass
        else:
            pass

    def unequip_item(self, equipment_type):
        """
        Unequip an item
        """
        pass

    def take_item(self, item_name):
        """
        Add an item to the inventory
        """

    def use_item(self, item_name):
        """
        Use an item from the inventory
        """
        pass

    def burn_item(self, item_name):
        """
        Destroy an inventory item
        """
        pass

if __name__ == '__main__':
    import monsters
    player = PlayerCharacter()
    skel = monsters.SkelWar()
    zom = monsters.Zombie()
    zom.die()
    skel.die()
    print player.get_score()
