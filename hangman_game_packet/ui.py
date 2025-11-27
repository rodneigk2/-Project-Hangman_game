import tkinter as tk

def build_ui(state, on_submit):
    window = tk.Tk()
    window.title("HANGMAN V1")
    window.geometry("500x420")

    tk.Label(window, text="Hangman Game", font=('Arial', 14)).pack()

    label_word = tk.Label(window, text=" ".join(state["lines"]), font=('Arial', 20))
    label_word.pack(pady=10)

    entry = tk.Entry(window, font='Arial', width=5)
    entry.pack(pady=10)
    
    attempts_label = tk.Label(window, text=f"Attempts: {state['attempts']}", font=('Ariel', 12))
    attempts_label.pack()

    wrong_label = tk.Label(window, text="Wrong letter: -", font=('Arial', 12))
    wrong_label.pack(pady=5)

    button = tk.Button(window, text=("TRY"),command=lambda: on_submit(entry, label_word, attempts_label, wrong_label, button))
    button.pack(pady=5)

    window.bind('<Return>', lambda e: on_submit(entry, label_word, attempts_label, wrong_label, button))

    return window