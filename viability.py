"""
This program contains the function used for determining if an army composition
is a viable counter to another army composition.
Requires the programs simulator.py and sim_units.py
"""
from simulator import combat_sim, get_health, get_damage
from sim_units import get_Units


def viability(enemy_comp, test_comp, test_type='units'):
    """
    Input is the enemy army composition, the army composition that
    we are testing, and the type of viablity test we are running.
    test_type is a string, either "units", "health", or "damage"
    Runs simulation 200 times. If the test army has at
    least 10% of its test type remaining 90% of the time, return 1
    Otherwise return 0
    """
    sim_count = 200
    Units = get_Units()
    test_limit = 0
    if test_type == 'units':
        unit_count = 0
        for unit in test_comp:
            unit_count += test_comp[unit]
        test_limit = 0.1 * unit_count
    
    if test_type == 'health':
        army_health = 0
        for unit in test_comp:
            unit_hp = Units[unit]['hp']
            army_health += unit_hp * test_comp[unit]
        test_limit = 0.1 * army_health
    if test_type == 'damage':
        army_dmg = 0
        for unit in test_comp:
            unit_dmg = Units[unit]['dps']
            army_dmg += unit_dmg * test_comp[unit]
        test_limit = 0.1 * army_dmg
    
    wins = 0
    sims = sim_count
    while sims > 0:
        test_army = combat_sim(enemy_comp, test_comp)
        if (test_type == 'units') and (len(test_army) > test_limit):
            wins += 1
        elif (test_type == 'health') and (get_health(test_army) > test_limit):
            wins += 1
        elif (test_type == 'damage') and (get_damage(test_army) > test_limit):
            wins += 1
        sims -= 1
    if (wins / sim_count) > 0.9:
        return 1
    else:
        return 0
