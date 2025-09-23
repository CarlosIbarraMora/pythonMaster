
import random

num = random.randint(1, 10)
ran_num = random.random() * 10 # Random float between 0 and 10
rand_float = random.uniform(1, 10) # Random float between 1 and 10

print(rand_float) # Output will be a random float between 1 and 10
print(ran_num) # Output will be a random float between 0 and 10
print(num) # Output will be a random integer between 1 and 10 (inclusive)
