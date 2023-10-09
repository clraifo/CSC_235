def introduction():                                                     # Function to introduce the program to the user
    print("\nWelcome to the Python Data Type Learning Application!\n")  # Print welcome message
    print("This application will introduce you to four fundamental Python data types: int, float, str, and bool.\n")    # Print explanation of the program

def explain_data_types():                                               # Function to explain the four data types  
    explanations = {                                                    # Dictionary of explanations for each data type
        "int": "An 'int' is an integer, like 1, 2, 3, -5, 0, etc.",     # Dictionary of data types and their explanations
        "float": "A 'float' is a decimal number, like 1.2, 3.14, -0.5, etc.",   # Dictionary keys are the data types
        "str": "A 'str' is a string, which means text. It's always enclosed in quotes, like 'hello', '123', 'Python', etc.", # Dictionary values are the explanations
        "bool": "A 'bool' is a boolean value, which can be either True or False."   # Dictionary is called 'explanations'
    }

    for data_type, explanation in explanations.items():                 # For loop to iterate through the dictionary
        print(f"{data_type.upper()}: {explanation}\n")                  # Print the data type and its explanation

introduction()                                                          # Call the introduction() function
explain_data_types()                                                    # Call the explain_data_types() function

import random                                                           # Import the random module

def ask_to_play():                                                      # Function to ask the user if they want to play
    response = input("Would you like to try identifying data type examples? (Y/N) ").lower()    # Ask the user if they want to play
    return response == 'y'                                              # Return True if the user enters 'y', False otherwise

def generate_random_example():                                          # Function to generate a random example   
    examples = {                                                        # Dictionary of examples for each data type
        "int": [1, 2, 3, -5, 0],                                        # Dictionary keys are the data types
        "float": [1.2, 3.14, -0.5, 0.0],                                # Dictionary values are lists of examples
        "str": ["hello", "123", "Python", "data type"],                 # Dictionary is called 'examples'
        "bool": [True, False]                                           # Dictionary is called 'examples'
    }
    
    data_type = random.choice(list(examples.keys()))                    # Choose a random data type
    example = random.choice(examples[data_type])                        # Choose a random example from the list of examples for that data type
    return data_type, example                                           # Return the data type and example

def main_interaction():                                                 # Function to run the main interaction of the program
    while True:
        data_type, example = generate_random_example()                  # Call the generate_random_example() function and assign the return values to variables
        print(f"\nHere's an example: {example}")                        # Print the example
        
        user_guess = input("Which data type is this? (int, float, str, bool) ").lower()     # Ask the user to guess the data type
        if user_guess == data_type:                                                         # Check if the user's guess is correct
            print("Correct! Well done.\n")                                                  # Print a message if the user's guess is correct                                                          
        else:                                                                               # If the user's guess is incorrect
            print(f"Oops! That's incorrect. The correct answer is {data_type}.\n")          # Print a message telling the user the correct answer
        
        try_again = input("Would you like to try again? (Y/N) ").lower()                    # Ask the user if they want to try again
        if try_again != 'y':                                                                # If the user doesn't want to try again
            print("Thanks for playing! Have a great day!")                                  # Print a goodbye message
            break                                                                           # Break out of the while loop

if ask_to_play():                   # Call the ask_to_play() function and check if the user wants to play
    main_interaction()              # Call the main_interaction() function if the user wants to play
