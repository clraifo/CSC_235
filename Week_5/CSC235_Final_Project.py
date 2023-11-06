import sys
import random
from PyQt5 import QtWidgets

class PasswordGeneratorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle('SecurePass Generator')
        self.setGeometry(100, 100, 280, 200)

        # Create the form elements
        self.create_form()

    def create_form(self):
        # Create the checkboxes
        self.checkBoxUppercase = QtWidgets.QCheckBox("Include Uppercase", self)
        self.checkBoxLowercase = QtWidgets.QCheckBox("Include Lowercase", self)
        self.checkBoxNumbers = QtWidgets.QCheckBox("Include Numbers", self)
        self.checkBoxSpecialChars = QtWidgets.QCheckBox("Include Special Characters", self)

        # Create the password length input
        self.spinBoxLength = QtWidgets.QSpinBox(self)
        self.spinBoxLength.setMinimum(7)  # Set minimum length to 7
        self.spinBoxLength.setMaximum(32)  # Set maximum length to 32
        self.spinBoxLength.setValue(12)  # Default length

        # Create the text edit for the password
        self.lineEditPassword = QtWidgets.QLineEdit(self)
        self.lineEditPassword.setReadOnly(True)  # Make the password field read-only

        # Create the buttons
        self.pushButtonGenerate = QtWidgets.QPushButton("Generate", self)
        self.pushButtonCopy = QtWidgets.QPushButton("Copy to Clipboard", self)

        # Set the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.checkBoxUppercase)
        layout.addWidget(self.checkBoxLowercase)
        layout.addWidget(self.checkBoxNumbers)
        layout.addWidget(self.checkBoxSpecialChars)
        layout.addWidget(self.spinBoxLength)
        layout.addWidget(self.lineEditPassword)
        layout.addWidget(self.pushButtonGenerate)
        layout.addWidget(self.pushButtonCopy)

        # Set the central widget and layout
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect buttons to their functions
        self.pushButtonGenerate.clicked.connect(self.generate_password)
        self.pushButtonCopy.clicked.connect(self.copy_to_clipboard)

    def generate_password(self):
        password_length = self.spinBoxLength.value()
        characters = {
            "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "lowercase": "abcdefghijklmnopqrstuvwxyz",
            "numbers": "0123456789",
            "special_chars": "!@#$%^&*()_+-=[]{}|;:'\",.<>/?"
        }
        
        options = {
            "uppercase": self.checkBoxUppercase.isChecked(),
            "lowercase": self.checkBoxLowercase.isChecked(),
            "numbers": self.checkBoxNumbers.isChecked(),
            "special_chars": self.checkBoxSpecialChars.isChecked()
        }

        if not any(options.values()):
            self.lineEditPassword.setText("Select at least one character type!")
            return

        password_chars = [characters[key] for key, value in options.items() if value]
        password_chars = ''.join(password_chars)
        generated_password = ''.join(random.choice(password_chars) for i in range(password_length))

        self.lineEditPassword.setText(generated_password)

    def copy_to_clipboard(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.lineEditPassword.text())

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
