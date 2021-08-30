
from pulp import *

"""
The Beer Distribution Problem for the PuLP Modeller
Authors: Antony Phillips, Dr Stuart Mitchell  2007
"""

# Creates a list of all the supply nodes
Warehouses = ['A', 'B']

# Creates a dictionary for the number of units of supply for each supply node
supply = {'A': 1000,
          'B': 4000}

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
costs = makeDict([Warehouses, Bars], costs, 0)
print()
print(costs)
# Creates the 'prob' variable to contain the problem data
prob = LpProblem('BeerDistributionProblem', LpMinimize)

# Creates a list of tuples containing all the possible routes for transport
Routes = [(w, b) for w in Warehouses for b in Bars]

# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts('Route', (Warehouses, Bars), 0, None, LpInteger)
print()
print(vars)
# print(vars)
# The objective function is added to 'prob' first
prob += lpSum([vars[w][b] * costs[w][b]] for w, b in Routes), 'Sum_of_Transporting_Costs'

# The supply maximum constraints are added to 'prob' for each supply node
for w in Warehouses:
    prob += lpSum([vars[w][b] * costs[w][b] for b in Bars]) <= supply[w], 'Sum_of_Products_out_of_Warehouse_%s' % w

# The demand minimum constraints are added to prob for each demand node (bar)
for b in Bars:
    prob += lpSum([vars[w][b] * costs[w][b] for w in Warehouses]) >= demand[b], 'Sum_of_products_into_Bars%s' % b

# prob.writeLP('BeerDistributionProblem.lp')
#
# prob.solve()
#
# # The status of the solution is printed to the screen
# print('Status: ', LpStatus[prob.status])
#
# # Each of the variables is printed with it's resolved optimum value
# for v in prob.variables():
#     print(f'{v.name}, = {v.varValue}')
#
# # The optimised objective function value is printed to the screen
# print("Total Cost of Transportation = ", value(prob.objective))







