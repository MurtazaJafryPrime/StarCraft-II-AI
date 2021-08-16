"""
This program uses a Monte Carlo simulation to randomly generate the
army compositions used in our linear program.
Requires the file sim_units.py and the random package
"""
import random
from sim_units import get_Units, get_Terran, get_Protoss, get_Zerg
import json


def init_army_comps(race, supply_cap=200, num_comps=1000):
    """
    Input is the race we wish to build army comps for
    race: 'Terran', 'Protoss', 'Zerg'
    Supply cap is an integer of the largest army size (default 200)
    num_comps is the number of army compositions we will generate
    Returns a list of num_comps randomly generated valid army compositions
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
    
    Units = get_Units()
    comps = []
    
    # initialize base format of an army composition
    base = {}
    for name in race_units:
        base[name] = 0
    count = 0
    while count < num_comps:
        comp = base.copy()
        # randomly generate an army comp
        # shuffle order of names, continuously update the
        # max number of units that can be randomly generated
        names = list(base.keys())
        random.shuffle(names)
        current_supply = supply_cap
        for name in names:
            max_unit = int(current_supply / Units[name]['supply'])
            if (get_army_supply(comp) <= current_supply) and (not extra_Motherships(comp)):
                comp[name] = random.randint(0, max_unit)
            current_supply -= get_army_supply(comp)
        
        temp_comp = comp.copy()
        # check that random comp is not already generated
        # only include valid comps
        if temp_comp not in comps:
            if (get_army_supply(temp_comp) <= supply_cap) and (not extra_Motherships(temp_comp)):
                comps.append(temp_comp)
                count += 1
    return comps


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


def get_Terran_comps():
    """
    Reads the file 'Terran_comps.json'
    Returns a list of dictionaries of all possible
    Terran army compositions
    """
    terran_comps = {}
    with open("Terran_comps.json", 'r') as read_file:
        terran_comps = json.load(read_file)
    return terran_comps


def get_Protoss_comps():
    """
    Reads the file 'Protoss_comps.json'
    Returns a list of dictionaries of all possible
    Protoss army compositions
    """
    protoss_comps = {}
    with open("Protoss_comps.json", 'r') as read_file:
        protoss_comps = json.load(read_file)
    return protoss_comps


def get_Zerg_comps():
    """
    Reads the file 'Zerg_comps.json'
    Returns a list of dictionaries of all possible
    Zerg army compositions
    """
    zerg_comps = {}
    with open("Zerg_comps.json", 'r') as read_file:
        zerg_comps = json.load(read_file)
    return zerg_comps


def generate_terran(supply_cap=200, num_comps=200):
    """
    Creates a list of terran armies saved as the file
    'Terran_comps.json'
    """
    with open('Terran_comps.json', 'w') as fout:
        json.dump(init_army_comps('Terran'), fout, indent=4)


def main():
    if True:
        generate_terran()
        print("Done with Terran")
    if True:
        with open('Protoss_comps.json', 'w') as fout:
            json.dump(init_army_comps('Protoss'), fout, indent=4)
        print("Done with Protoss")
    if True:
        with open('Zerg_comps.json', 'w') as fout:
            json.dump(init_army_comps('Zerg'), fout, indent=4)
        print("Done with Zerg")


if __name__ == "__main__":
    main()
