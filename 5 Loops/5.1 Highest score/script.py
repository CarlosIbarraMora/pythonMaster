students_score = [89, 20, 25, 30, 35, 40, 45, 89, 99, 100, 10, 53, 100, 66, 99]

highest_score = 0

for(score) in students_score:
    print(score)

for score in students_score:
    if score > highest_score:
        highest_score = score
    
print(f"The highest score in the class is: {highest_score}")