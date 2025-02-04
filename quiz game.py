print("Welcome to my computer quiz!")

playin = input("Do you want to play? ")

if playin.lower() != "yes":
    quit()
else: 
    print("Let's play!")

# Initialize score
score = 0

# Question 1
print("\nWhat does CPU stand for?")
print("a) Central Processing Unit")
print("b) Central Process Unit")
print("c) Central Processor Unit")
print("d) Central Program Unit")
answer = input("Choose the correct option (a/b/c/d): ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

# Question 2
print("\nWhat does GPU stand for?")
print("a) Graphics Processing Unit")
print("b) General Processing Unit")
print("c) Graphical Processor Unit")
print("d) General Purpose Unit")
answer = input("Choose the correct option (a/b/c/d): ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

# Question 3
print("\nWhich of the following is NOT a type of RAM?")
print("a) DRAM")
print("b) SRAM")
print("c) VRAM")
print("d) ROM")
answer = input("Choose the correct option (a/b/c/d): ")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

# Question 4
print("\nWhat is the purpose of a PSU in a computer?")
print("a) It cools the CPU")
print("b) It provides power to the motherboard")
print("c) It stores data for the computer")
print("d) It controls the computer's display output")
answer = input("Choose the correct option (a/b/c/d): ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

# Question 5
print("\nWhich of the following is the fastest type of storage?")
print("a) SSD")
print("b) HDD")
print("c) Optical Drive")
print("d) USB Flash Drive")
answer = input("Choose the correct option (a/b/c/d): ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

# Final score
print(f"\nYour final score is {score}/5.")
