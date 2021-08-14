"""
This file contains the funcitons needed to run the linear program that
finds an optimal counter-army.
Dependent upon the files viability.py, sim_units.py, simulator.py, and initialize_comps.py
along with the pyscipopt library.
"""

from pyscipopt import Model, quicksum
from viability import viability
from sim_units import get_Units, get_Terran, get_Protoss, get_Zerg
from simulator import combat_sim
from generate_comps import get_Terran_comps, get_Protoss_comps, get_Zerg_comps
from generate_comps import get_army_supply, init_army_comps
import time


def find_optimal_army(enemy_comp, test_type='cost', race='Terran', viab='units', supply_cap=200, min_supply=0):
    """
    Input is the army composition we are trying to optimize against
    test_type is a string, either "cost" or "time", determines what we
    are optimizing for. race is a string, either "Terran", "Protoss", or "Zerg",
    that we are creating our test army from.
    viab is a string, either 'units', 'health', or 'damage' that determines
    our viability function
    Finds an army composition of the given race that is the most efficent in terms of test_type
    Returns that optimal army composition as a string
    """
    start_time = time.time()
    army_model = Model("StarCraftII Army")
    comps = None
    if (race == 'Terran') or (race == 'Protoss') or (race == 'Zerg'):
        all_comps = init_army_comps(race, num_comps=100, supply_cap=supply_cap, min_supply=min_supply)
    else:
        error_message = "Race must be either 'Terran', 'Protoss', or 'Zerg'"
        return error_message
    
    # initialize binary variables for each comp that determines if
    # this comp can be picked or not
    picked_comps = {}
    for comp in all_comps:
        comp_name = str(comp)
        picked_comps[str(comp)] = army_model.addVar(vtype='B', name='Army Comp' + comp_name)
    
    for comp in all_comps:
        # constraint that army comps must be combat viable
        army_model.addCons(picked_comps[str(comp)] <= viability(enemy_comp, comp, viab))
        # constraint that army comps must be below supply cap
        army_model.addCons(picked_comps[str(comp)] * get_army_supply(comp) <= supply_cap)
    # only one comp should be chosen
    army_model.addCons(quicksum(picked_comps[str(comp)] for comp in all_comps) == 1)
    
    # objective function
    if test_type == 'cost':
        army_model.setObjective(quicksum(picked_comps[str(comp)]*get_army_cost(comp) for comp in all_comps), 'minimize')
    elif test_type == 'time':
        army_model.setObjective(quicksum(picked_comps[str(comp)]*get_army_time(comp) for comp in all_comps), 'minimize')
    
    # run linear program
    army_model.optimize()
    
    opt_comp = ""
    if army_model.getStatus() == "optimal":
         # find optimal comp and objective function value as a string
        for var in army_model.getVars():
            if (var.getLPSol() != 0):
                opt_comp += str(var) + ", " + test_type + "= " + str(army_model.getObjVal())
                opt_comp += ", viability:" + viab
    else:
        opt_comp = "No optimal army could be found"
    print(time.time() - start_time)
    return opt_comp


def get_army_cost(comp):
    """
    Input is an army compostion
    Returns the total cost of all units in that army
    Cost is calculated as the sum of each units mineral and gas costs
    """
    Units = get_Units()
    total_cost = 0
    for name in comp:
        unit_cost = Units[name]['mineral'] + Units[name]['gas']
        unit_count = comp[name]
        total_cost += unit_cost * unit_count
    return total_cost


def get_army_time(comp):
    """
    Input is an army composition
    Returns the total build time of all units in that army
    """
    Units = get_Units()
    total_time = 0
    for name in comp:
        unit_count = comp[name]
        unit_time = Units[name]['time']
        total_time += unit_time * unit_count
    return total_time
