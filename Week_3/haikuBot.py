"""
Core function of the haiku bot
  1. Takes a theme as input.
  2. Crafts a prompt for a Haiku based on the theme.
  3. Sends the prompt to the GPT-3 API.
  4. Retrieves and returns the generated Haiku.
"""

import tkinter as tk
import requests
import json

# Define the function to interact with GPT-3 API
def generate_haiku(theme, api_key):
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
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "OpenAI Python Client"
    }
    payload = {
        "prompt": prompt_text,
        "max_tokens": 50  # Limit the response length
    }
    
    # Make the API call
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    
    # Extract the generated text from the response
    haiku = response.json().get('choices', [{}])[0].get('text', '').strip()
    
    return haiku
# Define the function to be called when the "Generate" button is pressed
def on_generate():
    theme = theme_entry.get()
    try:
        haiku = generate_haiku(theme, "API_KEY_GOES_HERE")
        haiku_display.config(text=haiku)
    except requests.ConnectionError:
        haiku_display.config(text="Error connecting to the API. Check your internet connection.")
    except requests.Timeout:
        haiku_display.config(text="Request timed out. Please try again.")
    except requests.RequestException as e:  # Catch other requests exceptions
        haiku_display.config(text=f"An error occurred: {str(e)}")
    except Exception as e:
        haiku_display.config(text="An unexpected error occurred. Please try again.")


# Create the main application window
root = tk.Tk()
root.title("Haiku Generator")
root.resizable(False, False)  # Disable resizing of the window

# Create GUI components
theme_label = tk.Label(root, text="Enter a theme:")
theme_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate", command=on_generate)
haiku_display = tk.Label(root, wraplength=300)  # wraplength for better formatting

# Position the GUI components using a layout manager
theme_label.pack(pady=10)
theme_entry.pack(pady=10)
generate_button.pack(pady=10)
haiku_display.pack(pady=10)

# Start the application's main loop
root.mainloop()
