import random               # Import the random module
import string               # Import the string module

# Function to generate a block of 5 random letters
def generate_random_block():

    # uses the randon.choices() function to generate a random block of 5 letters based on the ascii_letters constant
    # using the k=5 parameter to specify the length of the block and then concatenates the block using the 
    # # join() function to join the block with a comma
    # this was NOT easy to get my head around
    return ''.join(random.choices(string.ascii_letters, k=5))       

# Function to create and write random blocks to a file
def write_blocks_to_file(filename, num_blocks):     # creates the function and initializes it with the filename and number of blocks
    with open(filename, 'w') as file:               # opens the file in write mode
        for _ in range(num_blocks):                 # loops through the number of blocks with the _ as a throwaway variable
            block = generate_random_block()         # calls the generate_random_block() function to generate a block
            file.write(block + ',')                 # Add a comma between blocks

# Function to read blocks from a file and display them with specific formatting
def read_blocks_from_file(filename):                    # creates the function and initializes it with the filename
    try:                                                # try block to catch errors
        with open(filename, 'r') as file:               # opens the file in read mode
            data = file.read()                          # reads the file and stores it in the data variable
            blocks = data.split(',')[:-1]               # Exclude the last empty string after the final comma
            for i, block in enumerate(blocks):          # loops through the blocks and uses the enumerate() function to get the index
                end_char = '   ' if i % 10 == 4 else ' '  # Three spaces between blocks 5 and 6, otherwise one space
                print(block + end_char, end='')         # Print blocks with the specified end character
                if (i + 1) % 10 == 0:                   # Every ten blocks, start a new line
                    print()                             # Newline after every ten blocks
    except FileNotFoundError:                           # exception handling for file not found
        print(f"The file {filename} was not found.")    # prints the error message
    except Exception as e:                              # exception handling for other errors
        print(f"An error occurred: {e}")                # prints an unhelpful error message

num_blocks = 10000                          # Number of blocks to generate

filename = "random_blocks.txt"              # Filename to write to and read from

write_blocks_to_file(filename, num_blocks)  # runs the write_blocks_to_file() function using the filename and number of blocks as parameters

read_blocks_from_file(filename)             # runs the read_blocks_from_file() function using the filename as a parameter
