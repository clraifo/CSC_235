"""
Core function of the haiku bot
  1. Takes a theme as input
  2. Crafts a prompt for a Haiku based on the theme
  3. Sends the prompt to the GPT-3 API
  4. Retrieves and returns the generated Haiku
  5. Has a GUI
"""

import tkinter as tk                # GUI library
import requests                     # HTTP library
import json                         # JSON library

def generate_haiku(theme, api_key): # Define the function to interact with GPT-3 API
    """
    Generate a haiku based on the provided theme using GPT-3.
    
    Parameters:
    - theme (str): The theme for the haiku.
    - api_key (str): The API key for GPT-3.
    
    Returns:
    - str: The generated haiku.
    """
    
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"     # Define the API endpoint
    
    
    prompt_text = f"Write a haiku about {theme}:"               # Craft the prompt for the Haiku
    
    headers = {                                                 # Define the headers
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",                     # The type of the data sent to the API
        "User-Agent": "OpenAI Python Client"                    # The type of the client
    }
    payload = {                                                 # Define the payload
        "prompt": prompt_text,                                  # The prompt for the API
        "max_tokens": 50                                        # Limit the response length
    }
    
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))       # Make the API call
    
    haiku = response.json().get('choices', [{}])[0].get('text', '').strip()             # Extract the generated text from the response
    
    return haiku                                                                        # here's your poem

def on_generate():                                              # Define the function to be called when the "Generate" button is pressed
    theme = theme_entry.get()                                   # Get the theme from the text entry
    try:
        haiku = generate_haiku(theme, "YOUR_OPENAI_API_KEY")    # Call the generate_haiku function with the theme and your API key
        haiku_display.config(text=haiku)                        # Display the generated haiku
    except requests.ConnectionError:                            # Catch connection errors
        haiku_display.config(text="Error connecting to the API. Check your internet connection.")   # Display an error message
    except requests.Timeout:                                                                # Catch timeouts
        haiku_display.config(text="Request timed out. Please try again.")                   # Display an error message
    except requests.RequestException as e:                                                  # Catch other requests exceptions
        haiku_display.config(text=f"An error occurred: {str(e)}")                           # Display an error message
    except Exception as e:                                                                  # Catch other exceptions
        haiku_display.config(text="An unexpected error occurred. Please try again.")        # Display an error message


# Create the main application window
root = tk.Tk()                      # Create the main application window
root.title("Haiku Generator")       # Set the title of the window
root.resizable(False, False)        # Disable resizing of the window

# Create GUI components
theme_label = tk.Label(root, text="Enter a theme:")                         # Create a label
theme_entry = tk.Entry(root)                                                # Create a text entry
generate_button = tk.Button(root, text="Generate", command=on_generate)     # Create a button
haiku_display = tk.Label(root, wraplength=300)                              # wraplength for better formatting

# Position the GUI components using a layout manager
theme_label.pack(pady=10)           # pady for padding, per every single tkinter tutorial in the internet
theme_entry.pack(pady=10)
generate_button.pack(pady=10)
haiku_display.pack(pady=10)

# Start the application's main loop
root.mainloop()
