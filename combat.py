import random
import os


import monsters
import player


class encounter(object):    
    def __init__(self, pc, enemy):
        mon_name = enemy.get_name()     # set enemy's name
        print "You see a: {}!".format(mon_name) + os.linesep
        print enemy
        self.battle()


    def battle(self):
        """
        Present the player character with options for the encounter
        """
        escape = False
        while pc.is_alive() and enemy.is_alive() and not escape:
            action = raw_input("What do you want to do? ")
            action = self._crop_input(action)
            if action == "a":
                self.attack(pc, enemy)
            elif action == "h":
                pc.heal_self()
            elif action == "m":
                self.magic(pc, enemy)
            elif action == "i":
                print "You have the following in your pouch:"
                print pc.get_inv()
            elif action == "s":
                print pc.get_player_status()
            elif action == '?':
                print "Available actions:" + os.linesep + \
                      "\t[A]ttack" + os.linesep + \
                      "\t[H]eal" + os.linesep + \
                      "\t[M]agic" + os.linesep + \
                      "\t[F]lee" + os.linesep + \
                      "\t[I]nventory" + os.linesep + \
                      "\t[S]tatus" + os.linesep
            elif action == "f":
                self.escape = flee(pc, enemy)
            else:
                print "Command not recognised. Please choose again"
                
        if not enemy.is_alive():         # if the enemy is dead
            print "The {} is defeated".format(enemy.get_name())
            print pc
        else:
            print "\r\n {}".format(pc.death())
        return

    @staticmethod  # Helper or utility function; independant of both class AND instance
    def _crop_input(action):
        if len(action) > 0:
            return action[0].lower()
        else:
            print "No input. Please choose again"        
            


    def attack(self, pc, enemy):
        """
        Fight the enemy using a physical attack
        (evades report a damage quantity)
        (enemy criticals not doing damage)
        """
        # Add an element of randomisation to prevent battles from being direct stat comparisons
        skill_test = pc.get_att() + random.randint(1, 10)
        enemy_skill_test = enemy.get_att() + random.randint(1, 10)

        attack_modifier = random.randint(-2, 2)             # More randomisation
        curse_roll = random.randint(1, 10)                  # the lower the better
        damage = 0

        if skill_test > enemy_skill_test:
            attacker = pc
            defender = enemy
            a_name = 'You'
            a_verb = ''
            d_name = enemy.get_name()
            d_verb = 's'
        else:
            attacker = enemy
            defender = pc
            a_name = enemy.get_name()
            a_verb = 's'
            d_name = 'You'
            d_verb = ''

        attack_power = attacker.get_att() + attack_modifier
        luck = attacker.get_stats()['LUCK']

        if attack > defender.DEF:                        # if pc's attack > enemy's defence
            damage = attack_power - defender.get_def()                   # base damage on the difference

        if curse_roll == 10:
            print "{} evade{} the attack!".format(d_name, d_verb)    # the defender evades the attack
        else:
            print "{} attack{}!".format(a_name, a_verb)
            if luck > curse_roll:                 # Deal extra damage if LUCK >= curse_roll
                crit_max = luck - curse_roll
                print "Critical hit!"
                damage += random.randint(1, crit_max)

            if damage < 0:                  # Prevent fights from healing
                damage = 0
            print "{} take{} {} damage".format(d_name, d_verb, damage)
            defender.take_damage(damage)
        if defender.is_alive():
            print "{}\r\n".format(defender)


    def magic(self, pc, enemy):
        """
        Use magic scroll to deal damage
        (does not currently reduce scroll quantity for misses and fumbles)
        (negative quantities of damage are possible)
        """
        if pc.has_item('scrollFire'):              # if pc has a fire scroll:
            # Add an element of randomisation to prevent battles from being direct stat comparisons
            skill_test = pc.get_wis() + random.randint(2, 12)
            enemy_skill_test = enemy.get_wis() + random.randint(1, enemy.get_dice_max())

            attack_modifier = random.randint(-2, 2)              # More randomisation
            curse_roll = random.randint(1, 10)                   # the lower the better

            magic_power = pc.get_wis() + attack_modifier

            if curse_roll == 10:
                damage = magic_power - int(pc.get_stats()['INT'] * 0.5)
                if damage < 0:                  # Prevent fights from healing
                    damage = 0
                print 'You fumble the spell and burn yourself, dealing {} points of damage.'.format(damage)
                pc.burn_item('scrollFire')
                print "{}\r\n".format(pc)
            elif skill_test > enemy_skill_test:
                damage = magic_power + 5 - enemy.get_wis()      # deal damage of wis + 5 (enemy defends with wis)
                if damage < 0:                                  # Prevent fights from healing
                    damage = 0

                pc.use_item('scrollFire', 'fire scroll', 'deal', damage, 'damage')
                enemy.take_damage(damage)
                print "{}\r\n".format(enemy)
            else:
                damage = int((enemy.get_att() - pc.get_def()) * 0.5) + attack_modifier
                print "Your shot goes wide and the {} lashes out, catching you with a glancing blow. " \
                      "You take {} points of damage.".format(enemy.get_name(), damage)
                pc.take_damage(damage)
                pc.burn_item('scrollFire')
                print "{}\r\n".format(pc)
        else:
            print "You do not have any Fire Scrolls"


    def flee(self):
        """
        Attempt to flee the encounter
        """
        skill_test = pc.ATT + random.randint(1, 10)
        enemy_skill_test = enemy.ATT + random.randint(1, 10)

        curse_roll = random.randint(1, 10)                  # the lower the better
        damage = enemy.get_att() + random.randint(-2, 2)

        if curse_roll == 10:
            print "You stumble, missing your chance to escape"
            return False
        else:
            if skill_test + pc.get_stats()['LUCK'] < enemy_skill_test + curse_roll:
                print "the {} takes advantage of your distraction and attacks as you flee!".format(
                    enemy.get_name(), damage)
                print "You take {} points of damage.".format(damage)
                pc.take_damage(damage)
            else:
                print "You escape unharmed"
            print "{}\r\n".format(pc)
            return True


if __name__ == '__main__':
    skel = monsters.SkelWar()
    zom = monsters.Zombie()
    dgn = monsters.Drake()
    pc = player.PlayerCharacter
    
    # player = actors.PlayerCharacter()
    # player.create_character()
    # player.character_template({'CHA': 1, 'AGL': 3, 'END': 2, 'INT': 7, 'PER': 2, 'STR': 3, 'LUCK': 7}, 35, 35)
    # encounter(player, skel)
    print pc.get_score()

    game = encounter(pc=pc, enemy=zom)
