"""
This program is used to process the randomly generated army compositions.
The goal is to generate graphs to show how well distributed those armies are.
"""
from generate_comps import get_Terran_comps, get_army_supply
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict


def unique_units(comps):
    """
    Input is list of army composition
    Returns a dictionary where keys:number of unique units in army,
    values:number of armies
    """
    unique = {}
    for comp in comps:
        count = get_unique(comp)
        if count in unique:
            unique[count] += 1
        else:
            unique[count] = 1
    return unique


def get_unique(comp):
    """
    comp: army composition
    Returns the number of unique units in that army
    """
    comp = comp.copy()
    count = 0
    for unit in comp:
        if comp[unit] > 0:
            count +=1
    return count


def supply_dist(comps):
    """
    Input is list of army composition
    Returns a dictionary where keys:supply of army,
    values:number of armies
    """
    supply_dist = {}
    for comp in comps:
        supply = get_army_supply(comp)
        if supply in supply_dist:
            supply_dist[supply] += 1
        else:
            supply_dist[supply] = 1
    return supply_dist


def build_graph(distr):
    """
    distr is output from either unique_units, supply_dist, or cost_dist
    name is string name of graph to be built
    """
    distr = distr.copy()
    sns.set()
    keys = list(distr.keys())
    # get values in the same order as keys, and parse percentage values
    vals  = [distr[k] for k in keys]
    sns.barplot(x=keys, y=vals)
    plt.title('Unique Units in 1000 randomly generated armies')
    plt.xlabel('Number of Unique Units')
    plt.ylabel("Armies")
    file_name = "Terran_Unique_Units.png"
    #plt.show()
    plt.savefig(file_name)


def build_histogram(comps):
    distr = supply_dist(comps)
    new_supply = []
    for supply in distr:
        for n in range(distr[supply]):
            new_supply.append(supply)
    sns.set()
    keys = list(distr.keys())
    sns.histplot(new_supply)
    plt.title('Army Supply in 1000 randomly generated armies')
    plt.xlabel('Supply')
    plt.ylabel('Armies')
    file_name = "Terran_Supply.png"
    #plt.show()
    plt.savefig(file_name)


def main():
    Terran = get_Terran_comps()
    build_histogram(Terran)
    build_graph(unique_units(Terran))


if __name__ == "__main__":
    main()
