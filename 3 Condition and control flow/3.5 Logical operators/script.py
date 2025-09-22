# Logical Operators Example

age = 20
has_ticket = True
is_sober = False

# Using 'and'
if age >= 18 and has_ticket:
    print("Allowed to enter the concert.")
else:
    print("Not allowed to enter the concert.")

# Using 'or'
if age < 18 or not has_ticket:
    print("Cannot enter: Either underage or no ticket.")
else:
    print("Entry requirements met.")

# Using 'not'
if not is_sober:
    print("Cannot enter: Not sober.")
else:
    print("Welcome! Enjoy the concert.")