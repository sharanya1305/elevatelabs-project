# Collect personal details for wordlist generation

name = input("Enter your name: ")
dob = input("Enter your year of birth: ")
pet = input("Enter your pet's name: ")
place = input("Enter a favorite place: ")

# Store all inputs in a list
inputs = [name, dob, pet, place]

# Print confirmation
print("\nDetails you entered:")
for item in inputs:
    print("-", item)
