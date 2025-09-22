len("Hello")

print(type("Hello")) #<class 'str'>

name_of_the_user = input("What is your name? ")
length_of_name = len(name_of_the_user)

print(type("Numer of characters in your name: ")) #<class 'str'>
print(type(length_of_name)) #<class 'int'>  

print("Your name has " + str(length_of_name) + " characters.")