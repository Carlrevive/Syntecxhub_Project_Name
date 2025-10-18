# Simple Calculator (Python)
A beginner-friendly Python calculator that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.  
Built as part of my learning journey in programming and problem-solving.

## 🚀 FEATURES
- Performs basic operations: `+`, `-`, `*`, `/`
- Handles invalid or unexpected inputs gracefully
- Displays clear results in the terminal
- Modular structure — calculation logic separated into functions
- Easy to extend with more operations (like power, modulus, etc.)

## Project Structure
calculator.py     # Main program file
README.md         # Project documentation

 CHALLENGES I FACED
User input issue:
Initially, I couldn’t enter values because VS Code was using the Output panel instead of the Terminal.
➤ Solution: Enabled “Run in Terminal” under Code Runner settings.
File outside repository error (Git):
Git kept saying the file was outside the repo when I tried git add.
➤ Solution: Moved the file inside the initialized repository folder before committing.
Division by zero crash:
Program crashed when dividing by zero.
➤ Solution: Added a condition to handle division by zero safely.
Suprisingly, i discovered a lot about defining functions and classes by going through
a series of errors before understanding in using them. At a point there were no errors in my codes but
still couldn't perform due to the wrong usage of functions creation and classes.

🧠LESSON LEARNED
How to separate logic from user interaction using functions
How to handle errors and exceptions in Python
Basic Git and GitHub workflow (adding, committing, pushing files)
How to write clear and structured documentation (like this README)

✨FUTURE IMPROVEMENT
Add support for more operations (e.g., exponentiation, square roots)
Create a simple graphical interface (Tkinter or PyQt)
Allow continuous calculations without restarting the program
