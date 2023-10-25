"""
Casey Raiford
CSC235 Python 1
25 Oct 2023

This program uses the GPT-3 API to generate a haiku based on a theme provided by the user. The logical 
flow of the program is as follows:

    1. The user provides a theme for the haiku.
    2. The program calls the GPT-3 API to generate a haiku based on the theme.
    3. The program displays the generated haiku to the user.

There three imports in the program:

    1. tkinter: This is the GUI library used to create the application window and the GUI components.
    2. requests: This is the HTTP library used to make the API call.
    3. json: This is the JSON library used to parse the API response.

There are two main functions in the program:

    1. generate_haiku: This function calls the GPT-3 API to generate a haiku based on the provided theme.
    2. on_generate: This function is called when the user clicks the "Generate" button. It gets the 
    theme from the text entry, calls generate_haiku, and displays the generated haiku.

>> Copilot wrote everything from line 6 to here <<
"""

import tkinter as tk            # GUI library
import requests                 # HTTP library
import json                     # JSON library

# Define the function to interact with GPT-3 API
def generate_haiku(theme, api_key):     # theme is the input, api_key is the key for the GPT-3 API
    """
    Generate a haiku based on the provided theme using GPT-3.
    
    Parameters:
    - theme (str): The theme for the haiku.
    - api_key (str): The API key for GPT-3.
    
    Returns:
    - str: The generated haiku.
    """
    
    # Define the API endpoint
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"
    
    # Craft the prompt for the Haiku
    prompt_text = f"Write a haiku about {theme}. The first line should have 5 syllables, the second line 7 syllables, and the third line 5 syllables.:"
    
    # Define the headers and payload for the API request
    headers = {
        "Authorization": f"Bearer {api_key}",       # Use the provided API key for authentication
        "Content-Type": "application/json",         # The type of the request body
        "User-Agent": "OpenAI Python Client"        # The type of the client
    }
    payload = {                         # The request body
        "prompt": prompt_text,          # The prompt for the Haiku
        "max_tokens": 50                # Limit the response length
    }
    
    # Make the API call
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    
    # Extract the generated text from the response
    haiku = response.json().get('choices', [{}])[0].get('text', '').strip()
    
    return haiku
# Define the function to be called when the "Generate" button is pressed
def on_generate():
    theme = theme_entry.get()               # Get the theme from the text entry
    try:
        haiku = generate_haiku(theme, "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")        # Call the function to generate the haiku
        haiku_display.config(text=haiku)                                                            # Display the generated haiku
    except requests.ConnectionError:                                                                # Catch connection errors
        haiku_display.config(text="Error connecting to the API. Check your internet connection.")   # Display an error message
    except requests.Timeout:                                                                        # Catch timeouts                                        
        haiku_display.config(text="Request timed out. Please try again.")                           # Display an error message
    except requests.RequestException as e:                                                          # Catch other requests exceptions
        haiku_display.config(text=f"An error occurred: {str(e)}")                                   # Display an error message
    except Exception as e:                                                                          # Catch other exceptions              
        haiku_display.config(text="An unexpected error occurred. Please try again.")                # Display an error message


# Create the main application window
root = tk.Tk()                  
root.title("Haiku Generator")   # Set the title of the window
root.resizable(False, False)    # Disable resizing of the window

# Create GUI components
theme_label = tk.Label(root, text="Enter a theme:")                     # Label for the text entry
theme_entry = tk.Entry(root)                                            # Text entry for the theme
generate_button = tk.Button(root, text="Generate", command=on_generate) # Button to generate the haiku
haiku_display = tk.Label(root, wraplength=300)                          # wraplength for better formatting

# Position the GUI components using a layout manager; pady is the vertical padding
theme_label.pack(pady=10)           # for the label
theme_entry.pack(pady=10)           # input window
generate_button.pack(pady=10)       # the button
haiku_display.pack(pady=10)         # the output window 

# Start the application's main loop
root.mainloop()
