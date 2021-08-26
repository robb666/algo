
from pulp import *
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

# A factory produces four different products, and that the daily produced amount of the first product is x₁,
# the amount produced of the second product is x₂, and so on. The goal is to determine the profit-maximizing daily
# production amount for each product, bearing in mind the following conditions:
#
#     The profit per unit of product is $20, $12, $40, and $25 for the first, second, third, and fourth product,
#     respectively.
#
#     Due to manpower constraints, the total number of units produced per day can’t exceed fifty.
#
#     For each unit of the first product, three units of the raw material A are consumed. Each unit of the second
#     product requires two units of the raw material A and one unit of the raw material B. Each unit of the third
#     product needs one unit of A and two units of B. Finally, each unit of the fourth product requires three
#     units of B.
#
#     Due to the transportation and storage constraints, the factory can consume up to one hundred units of the raw
#     material A and ninety units of B per day.


model = LpProblem(name='resource-allocation', sense=LpMaximize)

x = {i: LpVariable(name=f'x{i}', lowBound=0) for i in range(1, 5)}

model += (lpSum(x.values()) <= 50, 'manpower')
model += (3 * x[1] + 2 * x[2] + x[3] <= 100, 'material_a')
model += (x[2] + 2 * x[3] + 3 * x[4] <= 90, 'material_b')

model += 20 * x[1] + 12 * x[2] + 40 * x[3] + 25 * x[4]

status = model.solve()

print(f'status: {model.status}, {LpStatus[model.status]}')
print(f'objective: {model.objective.value()}')




































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
