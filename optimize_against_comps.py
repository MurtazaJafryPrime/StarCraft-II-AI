"""
This program is used for finding army counters for various types of
army compositions. The results are saved as txt files
"""
from sim_units import get_Units, get_Terran, get_Protoss, get_Zerg
from generate_comps import get_army_supply
from linear_program import find_optimal_army


def scale_comps(base_comps, supply_cap=200):
    """
    base_comps is a list of army composition that needs to be scaled up
    supply_cap is an integer that determines the max supply the armies
    will be scaled up to.
    This function scales each of the army compositions up the the max supply
    and adds those army compostitions into a dicitonary
    Returns that dictionary of scaled armies
    """
    scaled_comps = {}
    n = 1
    for base in base_comps:
        x = n
        m = 1
        # initialize the base army comp
        scaled_comps[x] = {}
        for name in base.keys():
            scaled_comps[x][name] = base[name]
        # add in scaled comps
        while get_army_supply(scaled_comps[n]) <= supply_cap:
            m += 1
            n += 1
            scaled_comps[n] = scaled_comps[x].copy()
            for key in scaled_comps[n]:
                scaled_comps[n][key] *= m
        if get_army_supply(scaled_comps[n]) > supply_cap:
            scaled_comps.pop(n)
            n -= 1
    return scaled_comps


def find_counters_from_list(army_list, name, supply_cap=200):
    """
    Input is a list of army compositions
    name is a string, name of txt file we will create and save our results to
    supply_cap is an integer of the largest army we wish to test
    Prints out the optimal army counters for each inputed army
    Creates a file
    """
    name = str
    terran_counters = {}
    protoss_counters = {}
    zerg_counters = {}
    for enemy in army_list.values():
        terran_counters[str(enemy)] = find_optimal_army(enemy, race='Terran', supply_cap=supply_cap)
        protoss_counters[str(enemy)] = find_optimal_army(enemy, race='Protoss', supply_cap=supply_cap)
        zerg_counters[str(enemy)] = find_optimal_army(enemy, race='Zerg', supply_cap=supply_cap)
    # Saves army counters in a text file
    file_name = name + ".txt"
    with open(file_name, 'w') as file:
        file.write("Terran Counters to " + name + " armies:")
        file.write('\n')
        for line in terran_counters:
            file.write(str(line))
            file.write('\n')
        file.write("Protoss Counters to " + name + " armies:")
        file.write('\n')
        for line in protoss_counters:
            file.write(str(line))
            file.write('\n')
        file.write("Zerg Counters to " + name + " armies:")
        file.write('\n')
        for line in zerg_counters:
            file.write(str(line))
            file.write('\n')


def create_terran_bio():
    """
    Returns the list of army comps related to the Terran Bio build
    """
    # Terran army compositions we wish to find counters to
    terran_bio_list = []
    # first ratio of 6:2:1 Marine:Marauder:Medivac
    terran_bio_1 = {}
    terran_bio_1['Marine'] = 6
    terran_bio_1['Marauder'] = 2
    terran_bio_1['Medivac'] = 1
    terran_bio_list.append(terran_bio_1)
    # second ratio of 15:5:2
    terran_bio_2 = {}
    terran_bio_2['Marine'] = 15
    terran_bio_2['Marauder'] = 5
    terran_bio_2['Medivac'] = 2
    terran_bio_list.append(terran_bio_2)
    terran_bio = scale_comps(terran_bio_list, supply_cap=200)

    return terran_bio


def create_skytoss():
    """
    Returns the list of skytoss army comps we wish to test
    """
    skytoss_list = []
    # first ratio of 3:2 Void Ray:Carrier
    skytoss_1 = {}
    skytoss_1['VoidRay'] = 3
    skytoss_1['Carrier'] = 2
    skytoss_list.append(skytoss_1)
    # second ratio of oops! all Carriers
    skytoss_2 = {}
    skytoss_2['VoidRay'] = 0
    skytoss_2['Carrier'] = 1
    skytoss_list.append(skytoss_2)
    skytoss = scale_comps(skytoss_list, supply_cap=200)


def create_zerg_comps():
    """
    Returns the zergling/roach/ravager comps we wish to test
    """
    ling_list = []
    # first ratio of 4:3:1 Zergling:Roach:Ravager
    ling_1 = {}
    ling_1['Zergling'] = 4
    ling_1['Roach'] = 3
    ling_1['Ravager'] = 1
    ling_list.append(ling_1)
    # second ratio of 2:1:1 Zergling:Roach:Ravager
    ling_2 = {}
    ling_2['Zergling'] = 2
    ling_2['Roach'] = 1
    ling_2['Ravager'] = 1
    ling_list.append(ling_2)
    zerg_rush = scale_comps(ling_list, supply_cap=200)


def main():
    terran_bio = create_terran_bio()
    skytoss = create_skytoss()
    zerg_rush = create_zerg_comps()
    find_counters_from_list(terran_bio, 'Terran Bio')
    find_counters_from_list(skytoss, 'Skytoss')
    find_counters_from_list(zerg_rush, 'Zerglings and Friends')


if __name__ == "__main__":
    main()
