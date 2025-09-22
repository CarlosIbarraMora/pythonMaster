total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

res = round((float(total) * (1 + int(tip) / 100)) / int(people), 2)
print(f"Each person should pay: ${res}")