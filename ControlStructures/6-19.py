computer_science = (input("SURVEY Are you interested in computer science? (y/n) "))
computer_games = (input("Do you like playing computer games? (y/n) "))
instagram = (input("Doyouhave instagram account? (y/n) "))

if computer_science == "y": computer_science = True
else: computer_science = False

if computer_games == "y": computer_games = True
else: computer_games = False

if instagram == "y": instagram = True
else: instagram = False

print("Survey results")
print(f"Like computer science? {computer_science}")
print(f"Like computer games? {computer_games}")
print(f"Have instagram?? {instagram}")