🎮 Hangman Game (Python + Tkinter)

A fully functional Hangman game built with Python and Tkinter.
The project is fully modularized into multiple files, following clean architecture and good practices — ideal for learning logic, UI, and Python structure.

🚀 Features

Validated input (repeated letters, non-letters, multiple letters, empty input)

GUI made with Tkinter

Dynamic ASCII hangman that updates with every mistake

Complete game state system in a separate module

Reset button that rebuilds the game state without closing the window

Full modularization:

game_logic.py → core game logic

hangman_ascii.py → proportional ASCII drawing

ui.py → interface builder

main.py → entry point

📁 Project Structure
/hangman-game
│
├── game_logic.py
├── hangman_ascii.py
├── ui.py
├── main.py
└── README.md

🧠 Module Responsibilities
game_logic.py

Contains:

create_state(word)

process_guess(state, letter)

Handles:

State initialization

Letter checking

Input validation

Error counting

Win/lose conditions

hangman_ascii.py

Contains:

The HANGMAN_PICS ASCII list

chose_hangman_stage(attempts_left, max_attempts)

Handles:

Selecting the correct hangman drawing

Works proportionally even if max_attempts changes

ui.py

Contains:

build_ui()

Handles:

Creating all Tkinter widgets

Linking UI components with the game logic

Automatic updates via update_visuals()

main.py

Runs the game:

Creates the initial state

Defines handle_submit() and on_reset()

Builds the UI

Starts Tkinter's mainloop()

▶️ How to Run

Make sure you have Python 3.9+ installed.

python main.py


The Tkinter window will open immediately.

📝 How to Play

Type a letter

Press TRY or hit ENTER

The hangman drawing updates automatically

You win or lose depending on your guesses

Click RESET to start again

🤓 Learning Goals

This project was designed to practice:

Modularization

Tkinter UI development

State management

Clean function-based architecture

ASCII rendering

Error handling

📌 Future Improvements

Add accent support (normalize input)

Add a start screen with custom word selection

Add scoring system

Add dark/light themes