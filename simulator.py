"""
This program includes methods used to simulate basic battle simulations
for the game StarCraft II
"""

import random
from sim_units import get_Units


Units = get_Units()


def combat_sim(army_comp1, army_comp2, MAX_ROUNDS=200):
    """
    Army 1 is enemy, Army 2 is test
    Input two army compositions written as dictionary with unit names as
    keys, unit counts as values. Simulates combat with the two army.
    The first army is assumed to be the enemy army, the second army is
    the army composition we are testing viability for.
    If combat takes longer than 200 seconds then it is assumed to be a
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
        build_Interceptor(army1)
        build_Interceptor(army2)
        track_Locust_Broodlings(army1)
        track_Locust_Broodlings(army2)
        rounds += 1
    
    if rounds >= MAX_ROUNDS:
        army2.clear()
    
    return army2


class Unit:
    """
    This class is used to represent each unit in an army
    """
    def __init__(self, name, army):
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
        # Carrier/Interceptor interaction
        if name == 'Carrier':
            self.child = {}
            for n in range(8):
                self.child[n] = Unit('Interceptor', army)
                army.append(self.child[n])
            # child_time is used to keep track of time until able to
            # build a new Interceptor child
            self.child_time = 0
        # SwarmHost/Locust interaction
        if name == 'SwarmHost':
            self.child = {}
            for n in range(2):
                self.child[n] = Unit('Locust', army)
                army.append(self.child[n])
        if name == 'Locust':
            self.live_time = 18
        # BroodLord/Broodling interaction
        if name == 'BroodLord':
            self.spawn_time = 0
        if name == 'Broodling':
            self.live_time = 6
    
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
            allies = army.copy()
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
            army.append(Unit(name, army))
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
        deal_unit_dps(unit, enemy_army, army)


def deal_unit_dps(unit, enemy_army, ally_army):
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
            # Banelings kill themselves after attacking
            if unit.name == 'Baneling':
                unit.hp = 0
        # BroodLords spawn Broodlings on hit, every 1.79 seconds
        # This will be rounded to spawn a Broodling every other round
        if unit.name == 'BroodLord':
            if unit.spawn_time == 0:
                ally_army.append(Unit('Broodling'))
                unit.spawn_time = 1
            else:
                unit.spawn_time -= 1
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
            deal_unit_dps(unit, enemy_army, army)


def remove_dead_units(army):
    """
    Input is a list of Units in an army
    Removes all Units with hp <=0 from that list
    Returns updated list
    """
    new_army = []
    # removes normal dead units
    for unit in army:
        if unit.hp >= 0:
            new_army.append(unit)
        # if Interceptor dies, free up that child space for the Carrier
        if unit.name == 'Carrier':
            for n in unit.child:
                if unit.child[n] is not None:
                    if unit.child[n].hp <= 0:
                        unit.child[n] = None
    # removes alive Interceptors if parent Carrier is dead
    for unit in army:
        if (unit.name == 'Carrier') and (unit.hp <= 0):
            for n in unit.child:
                if unit.child[n] in new_army:
                    new_army.remove(unit.child[n])
    return new_army


def build_Interceptor(army):
    """
    Input is an army.
    For every Carrier in that army, if an Interceptor
    slot is availible, build a new Interceptor and
    add that Interceptor back into the army
    """
    for unit in army:
        if unit.name == 'Carrier':
            for n in unit.child:
                if unit.child[n] is None:
                    if unit.child_time == 0:
                        unit.child[n] = Unit('Interceptor', army)
                        army.append(unit.child[n])
                        unit.child_time = 9


def track_Locust_Broodlings(army):
    """
    Input is a list of Units in an army
    Locusts can only live for 18 rounds and
    Broodlings can only live for 6 rounds
    Kills Locusts and Broodlings after exceeding their
    respective time limits
    """
    for unit in army:
        if unit.name == 'Locust':
            if unit.live_time <= 0:
                army.remove(unit)
            else:
                unit.live_time -= 1
        if unit.name == 'Broodling':
            if unit.live_time <= 0:
                army.remove(unit)
            else:
                unit.live_time -= 1
