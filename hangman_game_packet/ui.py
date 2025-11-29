import tkinter as tk
def build_ui(state, on_submit, on_reset):
    window = tk.Tk()
    window.title("HANGMAN GAME")
    window.geometry('500x320')
    window.resizable(False,False)

    tk.Label(window, text="Hangman game", font=('Arial', 12)).pack()
    
    label_word = tk.Label(window, text=" ".join(state['lines']), font=('Arial', 14))
    label_word.pack(pady=10)

    entry = tk.Entry(window, font=('Arial', 14), width=5, justify='center')
    entry.pack(pady=10)
    entry.focus_set()

    attempts_label = tk.Label(window, text=f"Attempts: {state['attempts']}", font=('Arial', 12))
    attempts_label.pack()

    wrong_label = tk.Label(window, text="WRONG LETTERS: -", font=('Arial', 12), wraplength=300, justify='left')
    wrong_label.pack(pady=5)

    button_try = tk.Button(
        window,
        text="TRY",
        command=lambda: on_submit(entry, label_word, attempts_label, wrong_label,button_try)
        )
    button_try.pack(pady=5)

    button_reset = tk.Button(
        window,
        text="RESET",
        command=lambda: on_reset(entry, label_word, attempts_label, wrong_label, button_try)
        )
    button_reset.pack(pady=5)

    window.bind('<Return>', lambda e: button_try.invoke())

    return window, entry, label_word, attempts_label, wrong_label, button_try, button_reset
