
from pulp import *

"""
The Beer Distribution Problem for the PuLP Modeller
Authors: Antony Phillips, Dr Stuart Mitchell  2007
"""

# Creates a list of all the supply nodes
Warehouses = ['A', 'B']

# Creates a dictionary for the number of units of supply for each supply node
supply = {'A': 1000, 'B': 4000}

# Creates a list of all demand nodes
Bars = ['1', '2', '3', '4', '5']

# Creates a dictionary for the number of units of demand
demand = {
    '1': 500,
    '2': 900,
    '3': 1800,
    '4': 200,
    '5': 700,
}

# Creates a list of costs of each transportation path
costs = [  # Bars
        # 1 2 3 4 5
        [2, 4, 5, 2, 1],  # A Warehouses
        [3, 1, 3, 2, 3],  # B
]

# The cost data is made into a dictionary
costs_dict = {
    'A': costs[0],
    'B': costs[1],
}

print(costs_dict['A'][0])

# prob = LpProblem('TransportationProblem', sense=LpMinimize)

# all_nodes = Warehouses + Bars

print(Warehouses.extend(Bars))

# all_nodes_dict = LpVariable.dict('all_nodes', all_nodes)










