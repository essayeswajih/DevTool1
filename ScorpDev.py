import sys
import subprocess
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtGui import QIcon, QColor, QPalette
from PyQt5.QtCore import Qt

def create_react_project(folder):
    print("Creating React project...")
    try:
        subprocess.run(["npx", "create-react-app", "react-client"], check=True, cwd=folder, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create React project. {e}")
        return

    subprocess.Popen(["npm", "start"], cwd=os.path.join(folder, "react-client"), shell=True)

def create_flask_project(folder):
    print("Creating Flask project...")
    flask_server_path = os.path.join(folder, "flask-server")
    try:
        subprocess.run(["mkdir", flask_server_path], check=True, shell=True)
        subprocess.run(["python", "-m", "venv", os.path.join(flask_server_path, "venv")], check=True, shell=True)
        subprocess.run([os.path.join(flask_server_path, "venv/Scripts/pip"), "install", "Flask"], check=True, shell=True)
        with open(os.path.join(flask_server_path, "app.py"), "w") as file:
            file.write('''from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)''')
        subprocess.Popen([os.path.join(flask_server_path, "venv/Scripts/flask"), "run"], cwd=flask_server_path, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create Flask project. {e}")
        return

def create_laravel_project(folder):
    print("Creating Laravel project...")
    try:
        subprocess.run(["composer", "create-project", "--prefer-dist", "laravel/laravel", folder], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create Laravel project. {e}")
        return

    print("Laravel project created successfully.")

def create_angular_project(folder):
    print("Creating Angular project...")
    try:
        subprocess.run(["ng", "new", "angular-client"], check=True, cwd=folder, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create Angular project. {e}")
        return

    subprocess.Popen(["ng", "serve"], cwd=os.path.join(folder, "angular-client"), shell=True)

def create_symfony_project(folder):
    print("Creating Symfony project...")
    try:
        subprocess.run(["composer", "create-project", "symfony/skeleton", folder], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to create Symfony project. {e}")
        return

    print("Symfony project created successfully.")

def open_laravel_project(folder):
    print("Opening Laravel project...")
    subprocess.Popen(["php", "artisan", "serve"], cwd=folder, shell=True)

def open_react_project(folder):
    print("Opening React project...")
    subprocess.Popen(["npm", "start"], cwd=os.path.join(folder, "react-client"), shell=True)

def open_flask_project(folder):
    print("Opening Flask project...")
    flask_server_path = os.path.join(folder, "flask-server")
    subprocess.Popen([os.path.join(flask_server_path, "venv/Scripts/flask"), "run"], cwd=flask_server_path, shell=True)

def open_angular_project(folder):
    print("Opening Angular project...")
    subprocess.Popen(["ng", "serve"], cwd=os.path.join(folder, "angular-client"), shell=True)

def open_symfony_project(folder):
    print("Opening Symfony project...")
    subprocess.Popen(["symfony", "server:start"], cwd=folder, shell=True)

class ProjectCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project Creator")
        self.setWindowIcon(QIcon("icon.png"))
        self.setStyleSheet("background-color: #F8F8F8;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        header_label = QLabel("Create or Open a Project")
        header_label.setStyleSheet(
            "font-size: 15px; font-weight: bold; margin-bottom: 15px; padding-top: 20px; color: #333333;"
        )
        layout.addWidget(header_label, alignment=Qt.AlignCenter)

        path_label = QLabel("Project Path:")
        path_label.setStyleSheet("font-size: 14px; margin-bottom: 5px;")
        self.path_input = QLineEdit()
        self.path_input.setStyleSheet("font-size: 14px; padding: 5px;")
        layout.addWidget(path_label)
        layout.addWidget(self.path_input)

        choice_label = QLabel("Choose a project:")
        choice_label.setStyleSheet("font-size: 14px; margin-bottom: 5px;")
        self.choice_combo = QComboBox()
        self.choice_combo.addItem("1. React project")
        self.choice_combo.addItem("2. Flask project")
        self.choice_combo.addItem("3. Laravel project")
        self.choice_combo.addItem("4. Angular project")
        self.choice_combo.addItem("5. Symfony project")
        self.choice_combo.setStyleSheet("font-size: 14px; padding: 5px;")
        layout.addWidget(choice_label)
        layout.addWidget(self.choice_combo)

        option_label = QLabel("Create or Open:")
        option_label.setStyleSheet("font-size: 14px; margin-bottom: 5px;")
        self.option_combo = QComboBox()
        self.option_combo.addItem("Create")
        self.option_combo.addItem("Open")
        self.option_combo.setStyleSheet("font-size: 14px; padding: 5px;")
        layout.addWidget(option_label)
        layout.addWidget(self.option_combo)

        create_button = QPushButton("Create Project")
        create_button.setStyleSheet(
            "QPushButton { background-color: #4caf50; color: white; padding: 8px; border: none; border-radius: 4px; font-size: 14px; }"
            "QPushButton:hover { background-color: #45a049; }"
        )
        create_button.clicked.connect(self.create_project)
        layout.addWidget(create_button, alignment=Qt.AlignCenter)

        layout.addStretch()

        footer_label = QLabel("ScorpDev - © 2023")
        footer_label.setStyleSheet("font-size: 12px; color: #888888; margin-top: 10px;")
        footer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer_label)

        # Apply visual enhancements
        self.setFixedSize(500, 350)  # Set a fixed window size
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#F8F8F8"))  # Set window background color
        self.setPalette(palette)

        self.setStyleSheet("QLabel { color: #333333; }")  # Adjust label color

    def create_project(self):
        folder = self.path_input.text()
        choice = self.choice_combo.currentText()
        option = self.option_combo.currentText()

        if not os.path.exists(folder):
            print("Error: Invalid path. Please provide a valid path.")
            return

        if choice == "1. React project" and option == "Create":
            create_react_project(folder)
        elif choice == "2. Flask project" and option == "Create":
            create_flask_project(folder)
        elif choice == "3. Laravel project" and option == "Create":
            create_laravel_project(folder)
        elif choice == "4. Angular project" and option == "Create":
            create_angular_project(folder)
        elif choice == "5. Symfony project" and option == "Create":
            create_symfony_project(folder)
        elif choice == "1. React project" and option == "Open":
            open_react_project(folder)
        elif choice == "2. Flask project" and option == "Open":
            open_flask_project(folder)
        elif choice == "3. Laravel project" and option == "Open":
            open_laravel_project(folder)
        elif choice == "4. Angular project" and option == "Open":
            open_angular_project(folder)
        elif choice == "5. Symfony project" and option == "Open":
            open_symfony_project(folder)
        else:
            print("Invalid choice. Exiting...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProjectCreator()
    window.show()
    sys.exit(app.exec_())
