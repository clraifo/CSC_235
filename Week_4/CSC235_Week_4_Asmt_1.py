import sys                          # Added to import sys
import random                       # Added to import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, 
                             QLineEdit, QMessageBox, QTextEdit)     

class FlashcardApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flashcards = {}  # This dictionary will store our flashcards
        self.load_flashcards()  # Load flashcards from file
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Flashcard App')

        # Create Flashcard Button
        self.create_btn = QPushButton('Create Flashcard', self)
        self.create_btn.resize(150, 40)
        self.create_btn.move(75, 50)
        self.create_btn.clicked.connect(self.create_flashcard)

        # Study Mode Button
        self.study_btn = QPushButton('Study Mode', self)
        self.study_btn.resize(150, 40)
        self.study_btn.move(75, 110)
        self.study_btn.clicked.connect(self.study_mode)

        # Window Settings
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def load_flashcards(self):
        try:
            with open("flashcards.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    question, answer = line.strip().split('|')
                    self.flashcards[question] = answer
        except FileNotFoundError:
            pass  # File doesn't exist yet, it will be created when saving a flashcard

    def save_flashcard_to_file(self, question, answer):
        with open("flashcards.txt", "a") as file:
            file.write(f"{question}|{answer}\n")

    def create_flashcard(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Create Flashcard")
        layout = QVBoxLayout()

        # Widgets for Question and Answer
        question_label = QLabel("Question:")
        self.question_input = QLineEdit()
        answer_label = QLabel("Answer:")
        self.answer_input = QLineEdit()
        save_button = QPushButton("Save Flashcard")
        save_button.clicked.connect(self.save_flashcard)

        # Add Widgets to the Dialog Layout
        layout.addWidget(question_label)
        layout.addWidget(self.question_input)
        layout.addWidget(answer_label)
        layout.addWidget(self.answer_input)
        layout.addWidget(save_button)
        
        dialog.setLayout(layout)
        dialog.exec_()

    def save_flashcard(self):
        question = self.question_input.text()
        answer = self.answer_input.text()

        if question and answer:  # Ensure both fields have input
            self.flashcards[question] = answer
            self.save_flashcard_to_file(question, answer)
            QMessageBox.information(self, "Success", "Flashcard saved successfully!")
        else:
            QMessageBox.warning(self, "Error", "Both fields must be filled!")

    def study_mode(self):
        if not self.flashcards:  # If no flashcards have been added
            QMessageBox.warning(self, "No Flashcards", "Please add some flashcards first.")
            return

        self.study_dialog = QDialog(self)
        self.study_dialog.setWindowTitle("Study Mode")
        layout = QVBoxLayout()

        self.card_display = QTextEdit()
        self.card_display.setReadOnly(True)
        self.flip_button = QPushButton("Flip")
        self.flip_button.clicked.connect(self.flip_card)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_flashcard)

        layout.addWidget(self.card_display)
        layout.addWidget(self.flip_button)
        layout.addWidget(self.next_button)

        self.study_dialog.setLayout(layout)
        
        self.current_question = random.choice(list(self.flashcards.keys()))
        self.card_display.setText(self.current_question)

        self.is_flipped = False  # To track if the card has been flipped or not

        self.study_dialog.exec_()

    def flip_card(self):
        if not self.is_flipped:
            self.card_display.setText(self.flashcards[self.current_question])
            self.is_flipped = True
        else:
            self.card_display.setText(self.current_question)
            self.is_flipped = False

    def next_flashcard(self):
        self.is_flipped = False
        self.current_question = random.choice(list(self.flashcards.keys()))
        self.card_display.setText(self.current_question)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlashcardApp()
    sys.exit(app.exec_())
