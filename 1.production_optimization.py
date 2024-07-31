from pulp import LpMaximize, LpProblem, LpVariable

# Create the model
model = LpProblem(name="beverage-production", sense=LpMaximize)

# Variables to be optimized, reprocents the number of units of each product
x1 = LpVariable(name="Lemonade", lowBound=0, cat='Integer')  # Lemonade
x2 = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')  # Juice

# Target function
model += (x1 + x2, "Total_Production")

# Limitations
model += (2 * x1 + x2 <= 100, "Water_Limit")  # Water
model += (x1 <= 50, "Sugar_Limit")  # Sugar
model += (x1 <= 30, "Lemon_Juice_Limit")  # Lemon Juice
model += (2 * x2 <= 40, "Fruit_Puree_Limit")  # Fruit Puree

# Solve the model
status = model.solve()

# Print the results
lemonade_produced = x1.value()
fruit_juice_produced = x2.value()
total_production = lemonade_produced + fruit_juice_produced

print(f"Produced Lemonade: {lemonade_produced}")
print(f"Produced Fruit Juice: {fruit_juice_produced}")
print(f"Total Production: {total_production}")
