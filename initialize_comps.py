"""
This program is used to generate all of the possible army compositions
possible for each of the three races in Starcraft II. Note that some
units are ommitted due to limitations of our simulator.
Army compositions are dictionaries with unit names as keys and the
number of units as values. Each race will have a list containing
all possible army composition dictionaries for that race.
These three lists will be saved as JSON files, named
Terran.json, Protoss.json, and Zerg.json

Note that this program takes an extremely long time to run, hence
saving the lists as JSON files so as to avoid running it more than once
"""

from sim_units import get_Units, get_Terran, get_Protoss, get_Zerg
from itertools import product
import json


def init_army_comps(race, supply_cap=200):
    """
    Input is the race we wish to build army comps for
    Creates a list of all possible army compositions with
    total supply <= supply_cap (default 200)
    Returns that list of army compositions
    """
    race_units = {}
    if race == 'Terran':
        race_units = list(get_Terran().keys())
    elif race == 'Protoss':
        race_units = list(get_Protoss().keys())
        # Intercceptors are a special case
        race_units.remove('Interceptor')
    elif race == 'Zerg':
        race_units = list(get_Zerg().keys())
        # Locust and Broodlings are special case
        race_units.remove('Locust')
        race_units.remove('Broodling')
    
    comps = []
    
    # create all possible combinations of army comps
    base = {}
    for name in race_units:
        base[name] = 0
    prod = product(range(supply_cap), repeat=len(base))
    prod = list(prod)
    for combo in prod:
        comp = base
        i = 0
        for n in base:
            comp[n] = combo[i]
            i += 1
            temp_comp = comp.copy()
            if temp_comp not in comps:
                comps.append(temp_comp)
    # remove all comps with more than one Mothership
    # or more than 200 supply
    for comp in comps:
        if (get_army_supply(comp) > supply_cap) or extra_Motherships(comp):
            comps.remove(comp)
    
    return comps


def extra_Motherships(comp):
    """
    Input is an army composition
    Returns True if more than one Mothership is
    in that army, else returns False
    """
    if 'Mothership' in comp:
        if comp['Mothership'] > 1:
            return True
    else:
        return False


def get_army_supply(comp):
    """
    Input is an army composition
    Returns the total supply used by that army
    """
    supply_total = 0
    Units = get_Units()
    for name in comp:
        supply = Units[name]['supply'] * comp[name]
        supply_total += supply
    return supply_total


def main():
    if False:
        with open('Terran_comps.json', 'w') as fout:
            json.dump(init_army_comps('Terran'), fout)
    if True:
        with open('Protoss_comps.json', 'w') as fout:
            json.dump(init_army_comps('Protoss'), fout)
    if False:
        with open('Zerg_comps.json', 'w') as fout:
            json.dump(init_army_comps('Zerg'), fout)

if __name__ == "__main__":
    main()