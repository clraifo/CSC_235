import random               # Import the random module
import string               # Import the string module

# Function to generate a block of 5 random letters
def generate_random_block():

    # uses the randon.choices() function to generate a random block of 5 letters based on the ascii_letters constant
    # using the k=5 parameter to specify the length of the block and then concatenates the block using the 
    # # join() function to join the block with a comma
    # this was NOT easy to get my head around
    # just saying
    return ''.join(random.choices(string.ascii_letters, k=5))       

# Function to create and write random blocks to a file
def write_blocks_to_file(filename, num_blocks):     
    with open(filename, 'w') as file:               
        for _ in range(num_blocks):                 
            block = generate_random_block()         
            file.write(block + ',')                 

# Function to read blocks from a file and display them with specific formatting
def read_blocks_from_file(filename):                    
    try:                                                
        with open(filename, 'r') as file:               
            data = file.read()                          
            blocks = data.split(',')[:-1]               
            for i, block in enumerate(blocks):          
                end_char = '   ' if i % 10 == 4 else ' '  
                print(block + end_char, end='')         
                if (i + 1) % 10 == 0:                   
                    print()            
        print(f"\nTotal number of blocks created: {len(blocks)}")   # prints the total number of blocks created
    except FileNotFoundError:                           
        print(f"The file {filename} was not found.")    
    except Exception as e:                              
        print(f"An error occurred: {e}")                

num_blocks = random.randint(5000, 15000)      # randomized number of blocks to generate between 5000 & 10000

filename = "random_blocks.txt"              # Filename to write to and read from

write_blocks_to_file(filename, num_blocks)  # runs the write_blocks_to_file() function using the filename and number of blocks as parameters

read_blocks_from_file(filename)             # runs the read_blocks_from_file() function using the filename as a parameter
