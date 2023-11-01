# Casey R.
# CSC235 Wk4 Assignment 1
# 20231101

import sys                          # Added to import sys
import random                       # Added to import random

# Added to import the following:
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, 
                             QLineEdit, QMessageBox, QTextEdit)     

class FlashcardApp(QMainWindow):        # Define class FlashcardApp

    # Initializes the application by setting up the flashcards dictionary, loading any saved flashcards from the file, and setting up the main user interface.
    def __init__(self):                 # Defines the function
        super().__init__()              # Call super().__init__()
        self.flashcards = {}            # dictionary to store flashcards
        self.load_flashcards()          # Load flashcards from file
        self.initUI()                   # Call self.initUI()

    # Loads flashcards from the file flashcards.txt and adds them to the flashcards dictionary.
    def initUI(self):                           # definitely a function
        self.setWindowTitle('Flashcard App')    # window title

        # Create Flashcard Button
        self.create_btn = QPushButton('Create Flashcard', self)
        self.create_btn.resize(150, 40)                             # resizes button
        self.create_btn.move(75, 50)                                # moves button
        self.create_btn.clicked.connect(self.create_flashcard)      # connects button to create_flashcard()

        # Study Mode Button
        self.study_btn = QPushButton('Study Mode', self)
        self.study_btn.resize(150, 40)                              # resizes button
        self.study_btn.move(75, 110)                                # moves button
        self.study_btn.clicked.connect(self.study_mode)             # connects button to study_mode()

        # Window Settings
        self.setGeometry(300, 300, 300, 200)    # Sets window geometry
        self.show()                             # shows the window

    # Attempts to load flashcards from a file named "flashcards.txt", parsing each line into a question and answer, and storing these in the flashcards dictionary.
    def load_flashcards(self):                                              # defines the function     
        try:                                                                                       
            with open("flashcards.txt", "r", encoding="utf-8") as file:     # opens flashcards.txt
                lines = file.readlines()                                    # reads lines
                for line in lines:                                          # for loop
                    question, answer = line.strip().split('|')              # splits line into question and answer
                    self.flashcards[question] = answer                      # adds question and answer to flashcards
        except FileNotFoundError:                                           # exceoption handling
            pass                                                            # if  flashcards.txt doesn't exist yet, it will be created when saving a flashcard
    
    # saves a flashcard to the file flashcards.txt
    def save_flashcard_to_file(self, question, answer):                     # defines save_flashcard_to_file()
        with open("flashcards.txt", "a") as file:                           # opens flashcards.txt
            file.write(f"{question}|{answer}\n")                            # writes question and answer to flashcards.txt

    # creates a dialog window for creating a flashcard, and adds the flashcard to the flashcards dictionary
    def create_flashcard(self):                                             # defines create_flashcard()    
        dialog = QDialog(self)                                              # creates dialog
        dialog.setWindowTitle("Create Flashcard")                           # sets dialog title
        layout = QVBoxLayout()                                              # creates layout

        # Widgets for Question and Answer
        question_label = QLabel("Question:")                    # question label
        self.question_input = QLineEdit()                       # question input
        answer_label = QLabel("Answer:")                        # answer label
        self.answer_input = QLineEdit()                         # answer input
        save_button = QPushButton("Save Flashcard")             # save button
        save_button.clicked.connect(self.save_flashcard)        # connects save button to save_flashcard()

        # Add Widgets to the Dialog Layout
        layout.addWidget(question_label)                # adds question label to layout
        layout.addWidget(self.question_input)           # adds question input to layout
        layout.addWidget(answer_label)                  # adds answer label to layout
        layout.addWidget(self.answer_input)             # adds answer input to layout
        layout.addWidget(save_button)                   # adds save button to layout
        
        dialog.setLayout(layout)                # sets dialog layout
        dialog.exec_()                          # executes dialog

    # Takes the entered question and answer, checks if both fields have data, then saves the new 
    # flashcard to the dictionary and the file. A confirmation or warning message is then displayed to the user.

    def save_flashcard(self):                   # defines the function
        question = self.question_input.text()   # gets question from question input
        answer = self.answer_input.text()       # gets answer from answer input

        if question and answer:                                                         # Ensure both fields have input
            self.flashcards[question] = answer                                          # adds question and answer to flashcards
            self.save_flashcard_to_file(question, answer)                               # calls save_flashcard_to_file()
            QMessageBox.information(self, "Success", "Flashcard saved successfully!")   # displays message box
        else:
            QMessageBox.warning(self, "Error", "Both fields must be filled!")           # displays error message box

    # creates a dialog window for studying  and displays a random flashcard
    def study_mode(self):                                                                       # defines study_mode() function
        if not self.flashcards:  # If no flashcards have been added                             # if no flashcards have been added
            QMessageBox.warning(self, "No Flashcards", "Please add some flashcards first.")     # displays message box
            return                                                                              # returns                                         

        self.study_dialog = QDialog(self)                   # creates dialog
        self.study_dialog.setWindowTitle("Study Mode")      # sets dialog title
        layout = QVBoxLayout()                              # creates layout

        self.card_display = QTextEdit()                         # creates text edit
        self.card_display.setReadOnly(True)                     # sets text edit to read only
        self.flip_button = QPushButton("Flip")                  # creates flip button
        self.flip_button.clicked.connect(self.flip_card)        # connects flip button to flip_card()
        self.next_button = QPushButton("Next")                  # creates next button
        self.next_button.clicked.connect(self.next_flashcard)   # connects next button to next_flashcard()

        layout.addWidget(self.card_display)     # adds card display to layout
        layout.addWidget(self.flip_button)      # adds flip button to layout
        layout.addWidget(self.next_button)      # adds next button to layout

        self.study_dialog.setLayout(layout)     # sets dialog layout
        
        self.current_question = random.choice(list(self.flashcards.keys()))     # gets random question from flashcards
        self.card_display.setText(self.current_question)                        # sets card display to current question

        self.is_flipped = False  # tracks whether the card has been flipped or not

        self.study_dialog.exec_()   # executes dialog

    # flips the flashcard to display the answer
    def flip_card(self):                                                        # defines the function
        if not self.is_flipped:                                                 # if card is not flipped
            self.card_display.setText(self.flashcards[self.current_question])   # sets card display to answer
            self.is_flipped = True                                              # sets is_flipped to True
        else:
            self.card_display.setText(self.current_question)                    # sets card display to question
            self.is_flipped = False                                             # sets is_flipped to False

    # displays the next flashcard
    def next_flashcard(self):                                                   # defines the function
        self.is_flipped = False                                                 # sets is_flipped to False
        self.current_question = random.choice(list(self.flashcards.keys()))     # gets random question from flashcards
        self.card_display.setText(self.current_question)                        # sets card display to current question

if __name__ == '__main__':          # if __name__ == '__main__':
    app = QApplication(sys.argv)    # app = QApplication(sys.argv)
    ex = FlashcardApp()             # ex = FlashcardApp()
    sys.exit(app.exec_())           # sys.exit(app.exec_())
