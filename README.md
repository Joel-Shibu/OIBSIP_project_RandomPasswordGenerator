# 🔐 Random Password Generator

A secure and user-friendly password generator application built with Python and Tkinter. This project was developed as part of an internship program to demonstrate modern Python GUI development and secure password generation techniques.

![Password Generator Screenshot](screenshot.png)

## ✨ Features

- Generate strong, cryptographically secure passwords
- Customize password length (8-64 characters)
- Include/exclude character types:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&*)
- One-click copy to clipboard

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Joel-Shibu/OIBSIP_project_RandomPasswordGenerator.git
   cd RandomPasswordGenerator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Customize your password:
   - Adjust the password length using the input field
   - Select which character types to include using the checkboxes
   - Click "Generate Password" to create a new password
   - Click "Copy to Clipboard" to copy the generated password

## 🛡️ Security

This application uses Python's built-in `secrets` module for cryptographically secure random number generation, ensuring that all generated passwords are secure and unpredictable.


---

Developed during the OIBSIP Internship Program
