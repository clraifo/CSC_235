# **********************First draft******************


import random

def main():
    print("Welcome to the Haunted House Adventure Game!")
    username = input("Please enter your screen name: ")

    print(f"Welcome, {username}! You find yourself standing in front of a creepy, old haunted house.")
    
    while True:
        print("You have three paths to choose from:")
        print("1. Enter through the front door.")
        print("2. Explore the garden on the left.")
        print("3. Check the dark alley on the right.")

        choice = input("Enter the number of your chosen path (1/2/3): ")

        if choice == '1':
            path_1(username)
            break
        elif choice == '2':
            path_2(username)
            break
        elif choice == '3':
            path_3(username)
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

def path_1(username):
    print(f"{username}, you enter the haunted house through the front door.")
    print("You encounter a locked door with a riddle on it.")
    print("Solve the riddle to proceed:")
    
    while True:
        answer = input("What has keys but can't open locks? ").lower()
        
        if answer == "piano":
            print("The door unlocks, and you proceed to the next challenge.")
            break
        else:
            print("That's not the correct answer. Try again.")

    print("You find yourself in a dimly lit room with a chest.")
    print("To open the chest, solve the anagram: 'TREASURE'.")
    
    while True:
        guess = input("Enter your guess: ").lower()
        
        if guess == "treasure":
            print("The chest opens, and you continue to the final challenge.")
            break
        else:
            print("That's not the correct answer. Try again.")

    print("You've reached the final room. There's a combination lock on the exit door.")
    print("To unlock it, guess the 4-digit combination (between 0000 and 9999).")
    
    correct_combination = str(random.randint(0, 9999)).zfill(4)
    
    while True:
        guess = input("Enter your 4-digit guess: ")
        
        if guess == correct_combination:
            print(f"The door unlocks, and you escape the haunted house, {username}! Congratulations!")
            break
        else:
            print("That's not the correct combination. Try again.")

def path_2(username):
    print(f"{username}, you decide to explore the garden on the left.")
    # Add path-specific story and puzzles here.

def path_3(username):
    print(f"{username}, you choose to check the dark alley on the right.")
    # Add path-specific story and puzzles here.

if __name__ == "__main__":
    main()
