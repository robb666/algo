
from pulp import *


# Case Studies
# https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html

"""
The Whiskas Model Python Formulation for the PuLP Modeller
Authors: Antony Phillips, Dr Stuart Mitchell  2007
"""

# Creates a list of the Ingredients
Ingredients = ['CHICKEN', 'BEEF', 'MUTTON', 'RICE', 'WHEAT', 'GEL']

# A dictionary of the costs of each of the Ingredients is created
costs = {
    'CHICKEN': 0.013,
    'BEEF': 0.008,
    'MUTTON': 0.010,
    'RICE': 0.002,
    'WHEAT': 0.005,
    'GEL': 0.001,
}

# A dictionary of the protein percent in each of the Ingredients is created
proteinPercent = {
    "CHICKEN": 0.100,
    "BEEF": 0.200,
    "MUTTON": 0.150,
    "RICE": 0.000,
    "WHEAT": 0.040,
    "GEL": 0.000,
}

# A dictionary of the fat percent in each of the Ingredients is created
fatPercent = {
    "CHICKEN": 0.080,
    "BEEF": 0.100,
    "MUTTON": 0.110,
    "RICE": 0.010,
    "WHEAT": 0.010,
    "GEL": 0.000,
}

# A dictionary of the fibre percent in each of the Ingredients is created
fibrePercent = {
    "CHICKEN": 0.001,
    "BEEF": 0.005,
    "MUTTON": 0.003,
    "RICE": 0.100,
    "WHEAT": 0.150,
    "GEL": 0.000,
}

# A dictionary of the salt percent in each of the Ingredients is created
saltPercent = {
    'CHICKEN': 0.002,
    'BEEF': 0.005,
    'MUTTON': 0.007,
    'RICE': 0.002,
    'WHEAT': 0.008,
    'GEL': 0.000
}

# Create the 'prob' variable to contain the problem data
prob = LpProblem('The_Whiskas_Problem', LpMinimize)

# A dictionary called 'ingredient_vars' is created to contain the referenced Variables
ingredient_vars = LpVariable.dicts('Ingri', Ingredients, 0)


print(ingredient_vars)

prob += lpSum([costs[i] * ingredient_vars[i] for i in Ingredients]), 'Total Cost of Ingredients per can'
print(prob)

prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 100, 'PercentagesSum'
prob += lpSum([proteinPercent[i] * ingredient_vars[i] for i in Ingredients]) >= 8.0, 'ProteinRequirement'
prob += lpSum([fatPercent[i] * ingredient_vars[i] for i in Ingredients]) >= 6.0, 'FatRequirement'
prob += lpSum([fibrePercent[i] * ingredient_vars[i] for i in Ingredients]) <= 2.0, 'FibreRequirement'
prob += lpSum([saltPercent[i] * ingredient_vars[i] for i in Ingredients]) <= 0.4, 'SaltRequirement'

# The problem data is written to an .lp file
prob.writeLP("WhiskasModel.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

print('Status: ', LpStatus[prob.status])


for v in prob.variables():
    print(v.name, '=', v.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of Ingredients per can = ", value(prob.objective))















# # A factory produces four different products, and that the daily produced amount of the first product is x₁,
# # the amount produced of the second product is x₂, and so on. The goal is to determine the profit-maximizing daily
# # production amount for each product, bearing in mind the following conditions:
# #
# #     The profit per unit of product is $20, $12, $40, and $25 for the first, second, third, and fourth product,
# #     respectively.
# #
# #     Due to manpower constraints, the total number of units produced per day can’t exceed fifty.
# #
# #     For each unit of the first product, three units of the raw material A are consumed. Each unit of the second
# #     product requires two units of the raw material A and one unit of the raw material B. Each unit of the third
# #     product needs one unit of A and two units of B. Finally, each unit of the fourth product requires three
# #     units of B.
# #
# #     Due to the transportation and storage constraints, the factory can consume up to one hundred units of the raw
# #     material A and ninety units of B per day.
#
#
# model = LpProblem(name='resource-allocation', sense=LpMaximize)
#
# # Definition od decision variables
# x = {i: LpVariable(name=f'x{i}', lowBound=0) for i in range(1, 5)}
# y = {i: LpVariable(name=f'y{i}', cat='Binary') for i in (1, 3)}
#
# # Add constraints
# model += (lpSum(x.values()) <= 50, 'manpower')
# model += (3 * x[1] + 2 * x[2] + x[3] <= 100, 'material_a')
# model += (x[2] + 2 * x[3] + 3 * x[4] <= 90, 'material_b')
#
# M = 100
# model += (x[1] <= y[1] * M, 'x1_constraint')
# model += (x[3] <= y[3] * M, 'x3_constraint')
# model += (y[1] + y[3] <= 1, 'y_constraint')
#
# # Set objective
# model += 20 * x[1] + 12 * x[2] + 40 * x[3] + 25 * x[4]
#
# status = model.solve()
#
# print(f'status: {model.status}, {LpStatus[model.status]}')
# print(f'objective: {model.objective.value()}')
#
# for var in model.variables():
#     print(f"{var.name}: {var.value()}")
#
# for name, constraint in model.constraints.items():
#     print(f"{name}: {constraint.value()}")












# # Create the model
# model = LpProblem(name="small-problem", sense=LpMaximize)
#
# # Initialize the decision variables
# x = LpVariable(name='x', lowBound=0, cat='Integer')
# y = LpVariable(name='y', lowBound=0)
#
#
# expression = 2 * x + 4 * y
# type(expression)
#
# constraint = 2 * x + 4 * y >= 8
# type(constraint)
#
# # Add the constraints to the model
# model += (2 * x + y <= 20, 'red_constraints')
# model += (4 * x - 5 * y >= -10, 'blue_constraints')
# model += (-x + 2 * y >= -2, 'yellow_constraints')
# model += (-x + 5 * y == 15, 'green_constraints')
#
# model += lpSum([x, 2 * y])
#
# # # Solve the problem
# status = model.solve()
#
# print(f"status: {model.status}, {LpStatus[model.status]}")
#
#
# print(f"objective: {model.objective.value()}")
#
#
# for var in model.variables():
#     print(f"{var.name}: {var.value()}")
#
#
# for name, constraint in model.constraints.items():
#     print(f"{name}: {constraint.value()}")
#
#
# print(model.solver)
