# In keeping with the season, I decided to make a Halloween-themed text adventure game.
# The game is a simple, linear story with three paths to choose from.
# Each path has a series of puzzles to solve before the player can proceed to the next challenge.
# The game is written in Python 3.10.2 and uses the time and random modules.
# The inspiration for this came to me as I was driving past a corn maze on my way home from work.
# Seriously, I looked over from a stoplight and thought, "Hey, I could use that for my homework"
# This is their website, for proper attribution: https://www.cornmaze.com/
# I wrote all of the cheesy dialogue myself, and I'm not ashamed to admit it
# I got the logic puzzles in path_3 here: https://parade.com/970343/parade/logic-puzzles/


print("\033[92m")   # Set text color to green because white is just so meh
congratulations_message = f"The door unlocks, and you escape the haunted house! Congratulations!"  # Define a global variable for the success message
import random       # Import the random module for generating random numbers
import time         # Import the time module for the global delay variable

global_delay = 1    # Defines a global delay variable so the text doesn't just blast out to console at once

def main():         # Defines the main function
    print("Welcome to the Haunted House Adventure Game!")   # Prints the welcome message
    time.sleep(global_delay)                                # 1 sec delay
    username = input("Please enter your screen name: ")     # Prompts the user for their name

    print(f"Welcome, {username}! You find yourself standing in front of a creepy, old haunted house.")  # Greets the user by name
    
    while True:                                             # Loops until the user enters a valid choice
        print("You have three paths to choose from:")       # Prints the choices
        time.sleep(global_delay)                            # Delays the next line of code by the global delay variable
        print("1. Enter through the front door.")           
        time.sleep(global_delay)                            # Delays the next line of code by the global delay variable
        print("2. Explore the garden on the left.")         
        time.sleep(global_delay)                            # Delays the next line of code by the global delay variable
        print("3. Check the dark alley on the right.")
        time.sleep(global_delay)                            # Delays the next line of code by the global delay variable

        choice = input("Enter the number of your chosen path (1/2/3): ")    # Prompts the user for their choice

        if choice == '1':                   # If the user chooses path 1, call the path_1 function
            path_1(username)                # Passes the username variable to the function
            break                           # Breaks out of the loop
        elif choice == '2':                 # If the user chooses path 2, call the path_2 function
            path_2(username)                # Passes the username variable to the function
            break                           # Breaks out of the loop
        elif choice == '3':                 # If the user chooses path 3, call the path_3 function
            path_3(username)                # Passes the username variable to the function
            break                           
        else:                                                                   # If the user enters an invalid choice
            print("Invalid choice. Please enter a valid option (1/2/3).")       # Print an error message

def path_1(username):                                                           # Defines the path_1 function
    print(f"{username}, you enter the haunted house through the front door.")   # Greets the user by name
    time.sleep(global_delay)                                                    # Delays the next line of code by the global delay variable
    print("You encounter a locked door with a riddle on it.")                   # Prints the story
    time.sleep(global_delay)                                                    # Delays the next line of code by the global delay variable
    print("Solve the riddle to proceed:")                                       # Prints the instructions
    time.sleep(global_delay)                                                    # Delays the next line of code by the global delay variable
    
    while True:                                                                     # Loops until the user enters the correct answer
        answer = input("What has keys but can't open locks (piano)? ").lower()      # Prompts the user for their answer
        time.sleep(global_delay)                                                    # Delays the next line of code by the global delay variable
        
        if answer == "piano":                                                   # If the user enters the correct answer
            print("The door unlocks, and you proceed to the next challenge.")   # Print a success message
            break                                                               # Break out of the loop
        else:                                                                   # If the user enters an incorrect answer
            print("That's not the correct answer. Try again.")                  # Print an error message
            time.sleep(global_delay)                                            # Delays the next line of code by the global delay variable

    print("You find yourself in a dimly lit room with a chest.")                # Prints the story
    time.sleep(global_delay)                                                    # Delays the next line of code by the global delay variable
    print("To open the chest, solve the anagram: 'RATSUREE'.")                  # Prints the instructions
    time.sleep(global_delay)                                                    # Delays the next line of code by the global delay variable
    
    while True:                                                         # Loops until the user enters the correct answer
        guess = input("Enter your guess (treasure): ").lower()          # Prompts the user for their answer
        time.sleep(global_delay)                                        # Delays the next line of code by the global delay variable
        
        if guess == "treasure":                                                 # If the user enters the correct answer
            print("The chest opens, and you continue to the final challenge.")  # Print a success message
            break                                                               # Break out of the loop                                                
        else:                                                                   # If the user enters an incorrect answer
            print("That's not the correct answer. Try again.")                  # Print an error message
            time.sleep(global_delay)                                            # Delays the next line of code by the global delay variable

    print("You've reached the final room. There's a combination lock on the exit door.")    # Prints the story
    time.sleep(global_delay)                                                                # Delays the next line of code by the global delay variable
    print("To unlock it, guess a number between 0 and 9).")                                 # Prints the instructions
    time.sleep(global_delay)                                                                # Delays the next line of code by the global delay variable
    
    correct_number = str(random.randint(0, 9))                                  # Generates a random number between 0 and 9 and converts it to a string
    
    while True:                                     # Loops until the user enters the correct answer
        guess = input("Enter your guess (0-9): ")   # Prompts the user for their answer
        
        if guess == correct_number:                 # If the user enters the correct answer
            print(congratulations_message)  # Print a success message
            break                                                                                       # Break out of the loop                                        
        elif guess.isdigit() and 0 <= int(guess) <= 9:                                                  # If the user enters an invalid answer
            print("That's not the correct number. Try again.")                                          # Print an error message
        else:                                                                                           # If the user enters an invalid answer                             
            print("Invalid input. Please enter a number between 0 and 9.")                              # Print an error message

def path_2(username):                                                                   # Defines the path_2 function
    print(f"{username}, you decide to explore the garden on the left.")                 # Greets the user by name
    time.sleep(global_delay)                                                            # Delays the next line of code by the global delay variable
    print("You find yourself in a garden filled with mysterious plants and statues.")   # Prints the story
    time.sleep(global_delay)                                                            # Delays the next line of code by the global delay variable
    
    print("Puzzle 1: Enter a number divisible by 3.")                       # Puzzle 1: Input a number divisible by 3
    time.sleep(global_delay)                                                # Delays the next line of code by the global delay variable
    
    while True:                                                             # Loops until the user enters a valid number
        number_guess = input("Enter a number (e.g. 3, 6, 9, etc): ")        # Prompts the user for their answer
        time.sleep(global_delay)                                            # Delays the next line of code by the global delay variable
        
        if number_guess.isdigit():                                          # If the user enters a valid number
            number_guess = int(number_guess)                                # Convert the input to an integer
            if number_guess % 3 == 0:                                       # If the number is divisible by 3
                print("Correct! You've solved the first puzzle.")           # Print a success message
                time.sleep(global_delay)                                    # Delays the next line of code by the global delay variable
                break                                                       # Break out of the loop
            else:                                                           # If the number is not divisible by 3
                print("That's not a number divisible by 3. Try again.")     # Print an error message
                time.sleep(global_delay)                                    # Delays the next line of code by the global delay variable
        else:                                                               # If the user enters an invalid answer
            print("Invalid input. Please enter a valid number.")            # Print an error message
            time.sleep(global_delay)                                        # Delays the next line of code by the global delay variable

    print("Puzzle 2: Solve the math problem: A + 5 = 15.")                  # Puzzle 2: Solve a simple math problem
    time.sleep(global_delay)                                                # Delays the next line of code by the global delay variable
    
    while True:                                                             # Loops until the user enters the correct answer
        math_guess = input("Enter the value of 'A' (10): ")                 # Prompts the user for their answer
        time.sleep(global_delay)                                            # Delays the next line of code by the global delay variable
        
        if math_guess.isdigit():                                            # If the user enters a valid number
            math_guess = int(math_guess)                                    # Convert the input to an integer
            if math_guess + 5 == 15:                                        # If the user enters the correct answer
                print("Correct! You've solved the second puzzle.")          # Print a success message
                time.sleep(global_delay)                                    # Delays the next line of code by the global delay variable
                break                                                       # Break out of the loop
            else:                                                           # If the user enters an incorrect answer
                print("That's not the correct answer. Try again.")          # Print an error message
                time.sleep(global_delay)                                    # Delays the next line of code by the global delay variable
        else:                                                               # If the user enters an invalid answer     
            print("Invalid input. Please enter a valid number.")            # Print an error message
            time.sleep(global_delay)                                        # Delays the next line of code by the global delay variable

    print("Puzzle 3: You come across a mysterious inscription on a stone tablet:")  # Puzzle 3: Solve the math problem
    time.sleep(global_delay)                                                        # Delays the next line of code by the global delay variable
    print("'If you take half of 30 and add 10, what do you get?'")                  # Prints the instructions
    time.sleep(global_delay)                                                        # Delays the next line of code by the global delay variable
    
    while True:                                                     # Loops until the user enters the correct answer
        math_guess = input("Enter your answer (25): ")              # Prompts the user for their answer
        time.sleep(global_delay)                                    # Delays the next line of code by the global delay variable
        
        if math_guess.isdigit():                                    # If the user enters a valid number
            math_guess = int(math_guess)                            # Convert the input to an integer
            if math_guess == 25:                                    # If the user enters the correct answer
                print("Correct! You've solved the third puzzle.")   # Print a success message
                time.sleep(global_delay)                            # Delays the next line of code by the global delay variable
                break                                               # Break out of the loop
            else:                                                   # If the user enters an incorrect answer
                print("That's not the correct answer. Try again.")  # Print an error message
                time.sleep(global_delay)                            # Delays the next line of code by the global delay variable
        else:                                                       # If the user enters an invalid answer
            print("Invalid input. Please enter a valid number.")    # Print an error message
            time.sleep(global_delay)                                # Delays the next line of code by the global delay variable

    print(congratulations_message)  # Print a success message    

def path_3(username):                                                                               # Defines the path_3 function
    print(f"{username}, you choose to check the dark alley on the right.")                          # Greets the user by name
    time.sleep(global_delay)                                                                        # Delays the next line of code by the global delay variable
    print("You find yourself in a dimly lit alley filled with mysterious symbols and puzzles.")     # Prints the story
    time.sleep(global_delay)                                                                        # Delays the next line of code by the global delay variable
        
    print("Puzzle 1: The day before two days after the day before tomorrow is Saturday.")           # Puzzle 1: Logic Puzzle 1
    time.sleep(global_delay)                                                                        # Delays the next line of code by the global delay variable
    print("What day is it today?")                                                                  # Prints the instructions
    time.sleep(global_delay)                                                                        # Delays the next line of code by the global delay variable
    
    while True:                                                                                     # Loops until the user enters the correct answer
        day_guess = input("Enter your answer (friday): ").strip().capitalize()                      # Prompts the user for their answer
        time.sleep(global_delay)                                                                    # Delays the next line of code by the global delay variable
        
        if day_guess == "Friday":                                                                   # If the user enters the correct answer
            print("Correct! You've solved the first logic puzzle.")                                 # Print a success message
            time.sleep(global_delay)                                                                # Delays the next line of code by the global delay variable
            break                                                                                   # Break out of the loop
        else:                                                                                       # If the user enters an incorrect answer
            print("That's not the correct answer. Try again.")                                      # Print an error message
            time.sleep(global_delay)                                                                # Delays the next line of code by the global delay variable
   
    print("Puzzle 2: Five people were eating apples: \n\nA finished before B, but behind C.")       # Puzzle 2: Logic Puzzle 2
    time.sleep(global_delay)                                                                        # Delays the next line of code by the global delay variable
    print("D finished before E, but behind B. \n\nWhat was the finishing order?\n")                 # Prints the instructions
    time.sleep(global_delay)                                                                        # Delays the next line of code by the global delay variable
    
    while True:                                                                                     # Loops until the user enters the correct answer
        order_guess = input("Enter the finishing order (CABDE): ").strip().upper()                  # Prompts the user for their answer
        time.sleep(global_delay)                                                                    # Delays the next line of code by the global delay variable
        
        if order_guess == "CABDE":                                                                  # If the user enters the correct answer
            time.sleep(global_delay)                                                                # Delays the next line of code by the global delay variable
            print("Correct! You've solved the second logic puzzle.\n")                              # Print a success message
            time.sleep(global_delay)                                                                # Delays the next line of code by the global delay variable
            break                                                                                   # Break out of the loop
        else:                                                                                       # If the user enters an incorrect answer
            print("That's not the correct answer. Try again.")                                      # Print an error message
            time.sleep(global_delay)                                                                # Delays the next line of code by the global delay variable
    
    print("Puzzle 3: \n\nThere are two ducks in front of a duck, two ducks behind a duck, and a duck in the middle.")   # Puzzle 3: Logic Puzzle 3
    time.sleep(global_delay)                                                                                            # Delays the next line of code by the global delay variable
    print("How many ducks are there?\n")                                                                                # Prints the instructions
    time.sleep(global_delay)                                                                                            # Delays the next line of code by the global delay variable
    
    while True:                                                                         # Loops until the user enters the correct answer
        duck_guess = input("Enter your answer (three): ").strip().capitalize()          # Prompts the user for their answer
        time.sleep(global_delay)                                                        # Delays the next line of code by the global delay variable
        
        if duck_guess == "Three":                                                       # If the user enters the correct answer
            print("Correct! You've solved the third logic puzzle.")                     # Print a success message
            time.sleep(global_delay)                                                    # Delays the next line of code by the global delay variable
            break                                                                       # Break out of the loop
        else:                                                                           # If the user enters an incorrect answer
            print("That's not the correct answer. Try again.")                          # Print an error message
            time.sleep(global_delay)                                                    # Delays the next line of code by the global delay variable                      

    print(congratulations_message)                                                      # Print a success message   

if __name__ == "__main__":                          # If the program is run directly
    main()                                          # Call the main function
