
from pulp import *
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name='x', lowBound=0, cat='Integer')
y = LpVariable(name='y', lowBound=0)


expression = 2 * x + 4 * y
type(expression)

constraint = 2 * x + 4 * y >= 8
type(constraint)

# Add the constraints to the model
model += (2 * x + y <= 20, 'red_constraints')
model += (4 * x - 5 * y >= -10, 'blue_constraints')
model += (-x + 2 * y >= -2, 'yellow_constraints')
model += (-x + 5 * y == 15, 'green_constraints')



model += lpSum([x, 2 * y])

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")


print(f"objective: {model.objective.value()}")


for var in model.variables():
    print(f"{var.name}: {var.value()}")


