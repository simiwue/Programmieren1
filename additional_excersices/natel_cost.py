cost_base = 22.98

cost_min = 0.248

minutes = input("How many minutes did you use the phone?")

print(f"Total costs are: {round(cost_base + cost_min * float(minutes), 2)} chf.")