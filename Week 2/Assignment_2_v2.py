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
    print("To unlock it, guess a number between 0 and 9).")
    
    correct_number = str(random.randint(0, 9))
    
    while True:
        guess = input("Enter your guess (0-9): ")
        
        if guess == correct_number:
            print(f"The door unlocks, and you escape the haunted house, {username}! Congratulations!")
            break
        elif guess.isdigit() and 0 <= int(guess) <= 9:
            print("That's not the correct number. Try again.")
        else:
            print("Invalid input. Please enter a number between 0 and 9.")

def path_2(username):
    print(f"{username}, you decide to explore the garden on the left.")
    print("You find yourself in a garden filled with mysterious plants and statues.")
    
    # Puzzle 1: Input a prime number
    print("Puzzle 1: Input a prime number.")
    
    while True:
        prime_guess = input("Enter a prime number: ")
        
        if prime_guess.isdigit():
            prime_guess = int(prime_guess)
            if is_prime(prime_guess):
                print("Correct! You've solved the first puzzle.")
                break
            else:
                print("That's not a prime number. Try again.")
        else:
            print("Invalid input. Please enter a valid number.")

    # Puzzle 2: Solve a simple math problem
    print("Puzzle 2: Solve the math problem: A + 5 = 15.")
    
    while True:
        math_guess = input("Enter the value of 'A': ")
        
        if math_guess.isdigit():
            math_guess = int(math_guess)
            if math_guess + 5 == 15:
                print("Correct! You've solved the second puzzle.")
                break
            else:
                print("That's not the correct answer. Try again.")
        else:
            print("Invalid input. Please enter a valid number.")

    # Puzzle 3: Solve the math problem
    print("Puzzle 3: You come across a mysterious inscription on a stone tablet:")
    print("'If you take half of 30 and add 10, what do you get?'")
    
    while True:
        math_guess = input("Enter your answer: ")
        
        if math_guess.isdigit():
            math_guess = int(math_guess)
            if math_guess == 25:
                print("Correct! You've solved the third puzzle.")
                break
            else:
                print("That's not the correct answer. Try again.")
        else:
            print("Invalid input. Please enter a valid number.")

    print("You've completed all the puzzles in the garden. You may now proceed further.")
    # Add more story elements or choices specific to this path.


def path_3(username):
    print(f"{username}, you choose to check the dark alley on the right.")
    print("You find yourself in a dimly lit alley filled with mysterious symbols and puzzles.")
    
    # Puzzle 1: Logic Puzzle 1
    print("Puzzle 1: The day before two days after the day before tomorrow is Saturday.")
    print("What day is it today?")
    
    while True:
        day_guess = input("Enter your answer (e.g., Monday, Tuesday, etc.): ").strip().capitalize()
        
        if day_guess == "Friday":
            print("Correct! You've solved the first logic puzzle.")
            break
        else:
            print("That's not the correct answer. Try again.")

    # Puzzle 2: Logic Puzzle 2
    print("Puzzle 2: Five people were eating apples, A finished before B, but behind C.")
    print("D finished before E, but behind B. What was the finishing order?")
    
    while True:
        order_guess = input("Enter the finishing order (e.g., CABDE): ").strip().upper()
        
        if order_guess == "CABDE":
            print("Correct! You've solved the second logic puzzle.")
            break
        else:
            print("That's not the correct answer. Try again.")

    # Puzzle 3: Logic Puzzle 3
    print("Puzzle 3: There are two ducks in front of a duck, two ducks behind a duck, and a duck in the middle.")
    print("How many ducks are there?")
    
    while True:
        duck_guess = input("Enter your answer (e.g., Three): ").strip().capitalize()
        
        if duck_guess == "Three":
            print("Correct! You've solved the third logic puzzle.")
            break
        else:
            print("That's not the correct answer. Try again.")

    print("You've successfully solved all the logic puzzles in the dark alley. You may now proceed further.")
    # Add more story elements or choices specific to this path.


if __name__ == "__main__":
    main()
