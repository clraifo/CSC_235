"""
This is a simple progam designed to teach the user to recognize four basic data types in Python.

    - It starts by defining and displaying an introduction to and explanation of the game.
    - Next, it imports the random module for Python to randomize examples picked
    - Asks the user to play
    - Picks a random data type (int, float, str, or bool)
    - Picks a random example from the list for that type
    - Displays it to the user
    - Assesses the user's answer
    - Displays congratulatikons or condelonces
    - Asks whether the user wants to paly again

random.org was used to generate the random numbers for the INT list
https://www.lddgo.net/en/string/randomnumber was used for the FLOAT list
https://bard.google.com/ was used to generate the random words for the STR list

"""

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
    examples = {                                                        
        
        # large set of INTS between -2000 and 2000
        "int": [-1998, -1987, -1872, -1819, -1747, -1724, -1620, -1576, -1500, -1422, -1354, -1081, -990, -986,     # dictionary of INT examples
                -859, -812, -769, -721, -696, -646, -631, -595, -563, -505, -414, -325, -252, -117, 59, 63, 
                387, 434, 444, 637, 901, 916, 1001, 1111, 1155, 1170, 1211, 1319, 1458, 1537, 1655, 1679, 
                1700, 1775, 1884, 1954],                                
        "float": [33.2627,   77.4039,   6.0686,   70.0330,   64.7930,   54.5252,   62.8744,   39.9176,   9.1075,   # dictionary of FLOAT examples
                  70.5580,  22.3014,  18.7676,   92.6266,   68.2334,   50.3795,   22.8857,   88.1022,   97.7460,   
                  46.3794,   33.4475,   41.3554,   64.0061,   5.5208,   17.8181,  33.9454,   29.6954,   56.3127,   
                  80.4952,   71.7956,   54.3867,   46.2378,   37.6108,   22.1798,   14.9972,   35.9465,   55.3027,   
                  22.8926,   45.2794,   9.2506,   42.0835,   30.7570,   66.8312,   19.2587,   28.9061,   94.9474,   
                  73.7832,   82.9703,   3.6076,   63.7773,   77.9822,   41.1944,   84.5985,   97.1352,   74.8831,   
                  75.8144,   16.5148,   59.5456,   95.2109,   16.6480,   5.4049,   73.9319,   41.2278,   45.3644,   
                  75.2279,   35.1615,   28.3817,   30.3255,   14.8941,   60.4618,   66.6853,   25.3177,   45.0930,   
                  91.1178,   41.1791,   77.7482,   47.8869,   82.1983,   7.4667,   72.3145,   99.4404,   32.5855,   
                  98.8173,   10.2492,   95.7938,   9.7106,   39.9117,   85.0437,   26.3031,   56.3524,   94.6571,
                  26.9500,   99.2823,   53.1158,   91.1924,   98.4789,   0.7794,   64.1837,   23.9471,   45.4422,],                                
        "str": ["jxiae", "emsddz", "bpfs", "cipha", "mmxvm", "scqtreh", "qqeqav", "tnjvdws", "xyqrb", "ghyoen",     # dictionary of STR examples
                "wimjgwg", "gsqy", "eohh", "xgjxvti", "nnklla", "hpgmc", "njm", "ftcp", "bdl", "lvxyeo", "ospt", 
                "xotb", "nqiipls", "mzx", "wcbsnqw", "zxtvj", "cirtx", "lmbdr", "lvn", "qhdpmm", "jrxb", "yys",
                  "rxeu", "snwtd", "pof", "owud", "zmbdy", "cenlfm", "vwwkuaj", "hgy", "bzgxvrt", "won", 
                  "atocfg", "ruac", "weeebj", "ejowge", "nmybm", "qbtcu", "tzjcapp", "tjm", "ggk", "ahrx", 
                  "imvvkl", "wpksw", "eewp", "zzl", "sbers", "lztby", "dck", "mpkfyq", "hdn", "janufg", "xzqejb", 
                  "mps", "ymiblq", "ffexdk", "artbeya", "ubuc", "pyy", "vbz", "mrqqzu", "gqhhfy", "scaeebn", 
                  "zaqgiyj", "pbuom", "zsgsuq", "brsxwc", "cexlfkl", "dqbtk", "fzhmyub", "wazrou", "trcyfr", 
                  "dor", "czrcd", "uhkepvf", "xio", "nftmrm", "stwsl", "aln", "dgei", "fjcb", "yjgnkl", "xlkxlk", 
                  "zgyjw", "fyw", "mlocuxu", "qmb", "rxnuzz", "lthlb", "hbvjk"
],                 
        "bool": [True, False]  # the list of bool values is pretty underwhelming by comparison
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
