"""
This program includes methods used to simulate basic battle simulations
for the game StarCraft II
"""

import random
from sim_units import get_Units


Units = get_Units()


def combat_sim(army_comp1, army_comp2, MAX_ROUNDS=600):
    """
    Input two army compositions written as dictionary with unit names as
    keys, unit counts as values. Simulates combat with the two army.
    The first army is assumed to be the enemy army, the second army is
    the army composition we are testing viability for.
    If combat takes longer than 10 minutes then it is assumed to be a
    stalemate and army2 is forcibly killed off
    Returns remaining army composition of army2
    """
    army1 = build_army(army_comp1)
    army2 = build_army(army_comp2)
    round1 = True
    rounds = 0
    while ((get_health(army1) > 0) and (get_health(army2) > 0)
          and (rounds <= MAX_ROUNDS)):
        if round1:
            deal_ranged_dps(army1, army2)
            deal_ranged_dps(army2, army1)
            round1 = False
        else:
            healing_units(army1)
            healing_units(army2)
            deal_damage(army1, army2)
            deal_damage(army2, army1)
        army1 = remove_dead_units(army1)
        army2 = remove_dead_units(army2)
        rounds += 1
    
    if rounds >= MAX_ROUNDS:
        army2.clear()
    
    return army2


class Unit:
    """
    This class is used to represent each unit in an army
    """
    def __init__(self, name):
        """
        Creates a new Unit object with the stats of the given name
        """
        self.name = name
        if Units[name]['armor'] > 0:
            self.hp = Units[name]['hp'] * Units[name]['armor'] * 1.5
        else:
            self.hp = Units[name]['hp']
        self.max_hp = self.hp
        self.dps = Units[name]['dps']
        self.ranged = Units[name]['ranged']
        self.attributes = Units[name]['attributes']
        self.type = Units[name]['type']
        self.targetable = Units[name]['targetable']
        self.bonuses = Units[name]['bonuses']
        self.bonus_dps = Units[name]['bonus_dps']
        self.time = Units[name]['time']
        self.healer = Units[name]['healer']
        # self.repaired is used only for healing units so that they cannot
        # repair and attack in the same round
        # repaired = True if Unit has repaired that round
        self.repaired = False
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str(self.name) + "_HP:" + str(self.hp)


def healing_units(army):
    """
    Input is a list of Units in an army
    If applicable, Units with the "healer" tag restore
    health to friendly Units in their army.
    Medivacs are allowed to split their healing, but we are
    restricting SCVs to only heal one target due to the
    variablity of the SCV repair ability
    """
    for unit in army:
        if unit.healer:
            allies = army
            allies.remove(unit)
            if unit.name == 'Medivac':
                heal = 12.6
                attribute = 'Biological'
                # Medivacs split their hps the same way other units can split dps
                while ((heal > 0) and (get_healable_units(allies, attribute) is not None)):
                    target = get_healable_units(allies, attribute)
                    restore = target.max_hp - target.hp
                    temp_heal = heal
                    heal -= restore
                    restore -= temp_heal
                    target.hp = target.max_hp - restore
                    # prevent overhealing
                    if target.hp > target.max_hp:
                        target.hp = target.max_hp
                    unit.repaired = True
            elif unit.name == 'SCV':
                # SCVs will only be allowed to repair a single target
                attribute = 'Mechanical'
                if get_healable_units(allies, attribute) is not None:
                    target = get_healable_units(allies, attribute)
                    heal = target.max_hp / target.time
                    target.hp += heal
                    # prevent overhealing
                    if target.hp > target.max_hp:
                        target.hp = target.max_hp
                    unit.repaired = True


def get_healable_units(allies, attribute):
    """
    Helper function to be used with healing_units
    allies is list of friendly Units, attribute is a string
    either "Biological" or "Mechanical" that determines the
    type of unit that can be healed
    Randomly chooses an allied Unit that can be healed
    returns that chosen Unit, returns None if no unit can be healed
    """
    heal_targets = []
    for ally in allies:
        if (attribute in ally.attributes) and (ally.hp < ally.max_hp):
            heal_targets.append(ally)
    if len(heal_targets) == 0:
        return None
    else:
        index = random.randint(0,len(heal_targets)-1)
        target = heal_targets[index]
        return target


def get_health(army):
    """
    Input is list of Units in an army
    Returns the sum of the remaining units in that army
    """
    health = 0
    for unit in army:
        health += unit.hp
    return health


def get_damage(army):
    """
    Input is a list of Units in an army
    Returns the total dps of that army
    """
    damage = 0
    for unit in army:
        damage += unit.dps
    return damage


def build_army(army_comp):
    """
    Input is a dictionary representing an army composition
    Returns a list of Units matching the army composition
    """
    army = []
    for name in army_comp:
        count = army_comp[name]
        while count >= 1:
            army.append(Unit(name))
            count -= 1
    return army


def get_attackable_unit(unit, enemy_army):
    """
    Input is attacking Unit and list of Units in enemy army
    Returns a random Unit in enemy army that attacking unit can attack
    If no enemy Unit can be attacked, return None
    """
    # create list of enemies unit can attack
    # targeting type (ground/air) and if enemy has hp>0
    enemies = []
    for enemy in enemy_army:
        if enemy.hp > 0:
            targetable = 0
            for target_type in unit.targetable:
                for enemy_type in enemy.type:
                    targetable += int(enemy_type == target_type)
            if targetable > 0:
                enemies.append(enemy)
    if len(enemies) == 0:
        return None
    else:
        # randomly chooses an enemy to attack
        index = random.randint(0,len(enemies)-1)
        enemy = enemies[index]
        return enemy


def deal_damage(army, enemy_army):
    """
    Input army is a list of attacking Units,
    enemy_army is list of Units being attacked.
    Calculates the damage dealt to enemy_army by all attacking units
    Updates the list of enemy Units with damaged health numbers
    """
    for unit in army:
        deal_unit_dps(unit, enemy_army)


def deal_unit_dps(unit, enemy_army):
    """
    Input is attacking Unit and list of Units being attacked
    Calculates the damage dealt to enemy army by the single unit
    Updates the list of enemy Units with damaged health numbers
    """
    if not unit.repaired:
        damage = unit.dps
        bonus_dmg = unit.bonus_dps
        while (damage > 0) and (get_attackable_unit(unit, enemy_army) is not None):
            enemy = get_attackable_unit(unit, enemy_army)
            # check for bonus damage. bonus damage is kept seperate from
            # normal damage
            bonus = 0
            # so long as there is some bonus dps to damage, check if
            # there is at least one matching attribute
            if bonus_dmg > 0:
                for bonus_att in unit.bonuses:
                    for att in enemy.attributes:
                        bonus += int(bonus_att == att)
            if bonus > 0:
                bonus_dmg_tmp = bonus_dmg
                bonus_dmg -= enemy.hp
                enemy.hp -= bonus_dmg_tmp
            dmg_temp = damage
            damage -= enemy.hp
            enemy.hp -= dmg_temp
    # reset repaired status for next round
    unit.repaired = False


def deal_ranged_dps(army, enemy_army):
    """
    Input army is a list of attacking Units,
    enemy_army is list of Units being attacked.
    Calculates the damage dealt to enemy_army only by ranged units
    Updates the list of enemy Units with damaged health numbers
    """
    for unit in army:
        if unit.ranged:
            deal_unit_dps(unit, enemy_army)


def remove_dead_units(army):
    """
    Input is a list of Units in an army
    Removes all Units with hp <=0 from that list
    Returns updated list
    """
    new_army = []
    for unit in army:
        if unit.hp >= 0:
            new_army.append(unit)
    return new_army

# unit stats hardcoded in here for testing only, delete later
def test_units():
    Terran_Units = {}
    Units = {}

    Marine = {}
    # Combat stats
    Marine['hp'] = 45
    Marine['dps'] = 9.8
    Marine['ranged'] = True
    Marine['armor'] = 0
    Marine['attributes'] = {'Biological', 'Light', 'Ground'}
    Marine['type'] = {'Ground'}
    Marine['targetable'] = {'Ground', 'Air'}
    Marine['bonuses'] = {}
    Marine['bonus_dps'] = 0
    Marine['healer'] = False
    # Resource stats
    Marine['mineral'] = 50
    Marine['gas'] = 0
    Marine['time'] = 18
    Marine['supply'] = 1
    Marine['race'] = 'Terran'

    Terran_Units['Marine'] = Marine
    Units['Marine'] = Marine

    SCV = {}
    # Combat stats
    SCV['hp'] = 45
    SCV['dps'] = 4.67
    SCV['ranged'] = False
    SCV['armor'] = 0
    SCV['attributes'] = {'Biological', 'Light', 'Mechanical', 'Ground'}
    SCV['targetable'] = {'Ground'}
    SCV['type'] = {'Ground'}
    SCV['bonuses'] = {}
    SCV['bonus_dps'] = 0
    SCV['healer'] = True
    # Resource stats
    SCV['mineral'] = 75
    SCV['gas'] = 0
    SCV['time'] = 12
    SCV['supply'] = 1
    SCV['race'] = 'Terran'
    Terran_Units['SCV'] = SCV
    Units['SCV'] = SCV

    Medivac = {}
    # Combat stats
    Medivac['hp'] = 150
    Medivac['dps'] = 0
    Medivac['ranged'] = False
    Medivac['armor'] = 1
    Medivac['attributes'] = {'Armored', 'Mechanical', 'Air'}
    Medivac['targetable'] = {}
    Medivac['type'] = {'Air'}
    Medivac['bonuses'] = {}
    Medivac['bonus_dps'] = 0
    Medivac['healer'] = True
    # Resource stats
    Medivac['mineral'] = 100
    Medivac['gas'] = 100
    Medivac['time'] = 30
    Medivac['supply'] = 2
    Medivac['race'] = 'Terran'
    Terran_Units['Medivac'] = Medivac
    Units['Medivac'] = Medivac

    Hellion = {}
    # Combat stats
    Hellion['hp'] = 90
    Hellion['dps'] = 4.48*5
    Hellion['ranged'] = True
    Hellion['armor'] = 0
    Hellion['attributes'] = {'Light', 'Mechanical', 'Ground'}
    Hellion['targetable'] = {'Ground'}
    Hellion['type'] = {'Ground'}
    Hellion['bonuses'] = {'Light'}
    Hellion['bonus_dps'] = 3.4*5
    Hellion['healer'] = False
    # Resource stats
    Hellion['mineral'] = 100
    Hellion['gas'] = 0
    Hellion['time'] = 21
    Hellion['supply'] = 2
    Hellion['race'] = 'Terran'
    Terran_Units['Hellion'] = Hellion
    Units['Hellion'] = Hellion

    return Units