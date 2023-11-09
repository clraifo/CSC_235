# Casey L. Raiford
# CSC235 20231108
# Criteria
# Has instruction dialogue in app window, and an error message if no character types are selected
# Takes user input for 4 chracter types and password length
# Outputs a password to the app window
# Uses strings, bools, and ints
# Has 5 functions
# Has a dictionary and a list comprehension 

import sys                      # Import the sys module 
import random                   # Import the random module
from PyQt5 import QtWidgets     # Import the PyQt5 module

class PasswordGeneratorApp(QtWidgets.QMainWindow):      # Create the PasswordGeneratorApp class
    def __init__(self):                                 # defines the __init__ function
        super().__init__()                              # calls parent class __init__ function

        # Set the window properties
        self.setWindowTitle('SecurePass Generator')     # sets the window title
        self.setGeometry(100, 100, 280, 200)            # defines the window size

        self.create_form()                             # calls the create_form function

    def create_form(self):                            # degines the create_form function
        # Create the checkboxes
        self.checkBoxUppercase = QtWidgets.QCheckBox("Include Uppercase", self)                 # Create the checkbox for uppercase letters
        self.checkBoxLowercase = QtWidgets.QCheckBox("Include Lowercase", self)                 # Create the checkbox for lowercase letters
        self.checkBoxNumbers = QtWidgets.QCheckBox("Include Numbers", self)                     # Create the checkbox for numbers
        self.checkBoxSpecialChars = QtWidgets.QCheckBox("Include Special Characters", self)     # Create the checkbox for special characters

        # Create the password length input
        self.spinBoxLength = QtWidgets.QSpinBox(self)       # Create the spinbox for the password length
        self.spinBoxLength.setMinimum(7)                    # Set minimum length to 7
        self.spinBoxLength.setMaximum(32)                   # Set maximum length to 32
        self.spinBoxLength.setValue(16)                     # Default length, I changed this after the video to 16

        # Create the text edit for the password
        self.lineEditPassword = QtWidgets.QLineEdit(self)   # Create the line edit for the password
        self.lineEditPassword.setReadOnly(True)             # Make the password field read-only

        # Create the buttons
        self.pushButtonGenerate = QtWidgets.QPushButton("Generate", self)       # generate button
        self.pushButtonCopy = QtWidgets.QPushButton("Copy to Clipboard", self)  # copy button

        # Set the layout
        layout = QtWidgets.QVBoxLayout()            # Create a vertical layout    
        layout.addWidget(self.checkBoxUppercase)    # uppercase checkbox 
        layout.addWidget(self.checkBoxLowercase)    # lowercase checkbox 
        layout.addWidget(self.checkBoxNumbers)      # numbers checkbox 
        layout.addWidget(self.checkBoxSpecialChars) # special characters checkbox
        layout.addWidget(self.spinBoxLength)        # password length spinbox
        layout.addWidget(self.lineEditPassword)     # password line edit
        layout.addWidget(self.pushButtonGenerate)   # generate button 
        layout.addWidget(self.pushButtonCopy)       # copy button 

        # Set the central widget and layout
        central_widget = QtWidgets.QWidget()        # Create a central widget
        central_widget.setLayout(layout)            # Set the layout for the central widget
        self.setCentralWidget(central_widget)       # Set the central widget

        # Connect buttons to their functions
        self.pushButtonGenerate.clicked.connect(self.generate_password) 
        self.pushButtonCopy.clicked.connect(self.copy_to_clipboard)

    def generate_password(self):                                # Define the generate_password function
        password_length = self.spinBoxLength.value()            # Get the password length from the spinbox
        characters = {                                          # Define the characters dictionary
            "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",          # uppercase chractrers
            "lowercase": "abcdefghijklmnopqrstuvwxyz",          # lowercase characters
            "numbers": "0123456789",                            # numbers
            "special_chars": "!@#$%^&*()_+-=[]{}|;:'\",.<>/?"   # special characters. I'm pretty sure some of these won't work in a password, 
                                                                # but I threw them all in thinking  I could remove them later if needed.
                                                                # turns out they work in this app, but I assume the \ would cause problems at a minimum
        }
        
        options = {                                                     # Define the options dictionary
            "uppercase": self.checkBoxUppercase.isChecked(),            # uppercase checkbox
            "lowercase": self.checkBoxLowercase.isChecked(),            # lowercase checkbox
            "numbers": self.checkBoxNumbers.isChecked(),                # numbers checkbox
            "special_chars": self.checkBoxSpecialChars.isChecked()      # special characters checkbox
        }

        if not any(options.values()):                                               # if no options are selected
            self.lineEditPassword.setText("Select at least one character type!")    # the user gets this error message
            return                                                                  # and the function ends

        password_chars = [characters[key] for key, value in options.items() if value]                   # Create a list of characters based on the options selected
        password_chars = ''.join(password_chars)                                                        # joins  the list of characters into a string
        generated_password = ''.join(random.choice(password_chars) for i in range(password_length))     # Generate the password

        self.lineEditPassword.setText(generated_password)                                               # Set the password line edit to the generated password

    def copy_to_clipboard(self):                            # Define the copy_to_clipboard function
        clipboard = QtWidgets.QApplication.clipboard()      # creates a clipboard object
        clipboard.setText(self.lineEditPassword.text())     # Set the clipboard text to the password line edit text

def main():                                     # this is definitely the main function 
    app = QtWidgets.QApplication(sys.argv)      # create the application object
    window = PasswordGeneratorApp()             # creates the PasswordGeneratorApp object
    window.show()                               # shows the window
    sys.exit(app.exec_())                       # executes the application

if __name__ == '__main__':                  # If this is the main module
    main()                                  # Call the main function
