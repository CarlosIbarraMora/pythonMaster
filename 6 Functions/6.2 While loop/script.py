# Comparing for vs while loops in Python

print("=== Example 1: Basic Counting ===")
print("Using for loop:")
for i in range(5):   # iterate over a fixed range
    print(i, end=" ")
print()

print("Using while loop:")
i = 0
while i < 5:         # iterate while condition is True
    print(i, end=" ")
    i += 1
print("\n")


print("=== Example 2: Iterating over a collection ===")
fruits = ["apple", "banana", "cherry"]

print("Using for loop:")
for fruit in fruits:   # directly iterate over list elements
    print(fruit)

print("Using while loop:")
i = 0
while i < len(fruits):  # need index management
    print(fruits[i])
    i += 1
print()


print("=== Example 3: Loop with condition until event happens ===")
print("While loop is better here (unknown number of iterations):")
number = 1
while number < 1000:  # keep doubling until condition fails
    print(number, end=" ")
    number *= 2
print("\n")

print("For loop alternative (less natural here):")
for _ in range(20):  # we need an artificial upper bound
    if number >= 1000:
        break
    print(number, end=" ")
    number *= 2
print("\n")


print("=== Example 4: Properties & Use Cases ===")
print("- For loops are best when you know the exact range/collection to iterate.")
print("- While loops are best when the number of iterations is not known beforehand.")
print("- For loops are generally more concise; while loops give more control.")
