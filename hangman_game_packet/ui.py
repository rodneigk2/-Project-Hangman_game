import tkinter as tk
from hangman_ascii import chose_hangman_stage 

def build_ui(state, on_submit, on_reset):
    window = tk.Tk()
    window.title("HANGMAN GAME")
    window.geometry('500x320')
    window.resizable(False,False)

    tk.Label(window, text="Hangman game", font=('Arial', 12)).pack(pady=6)

    top = tk.Frame(window)
    top.pack(fill='x', padx=8, pady=4)

    hangman_label = tk.Label(
        top,
        text=chose_hangman_stage(state.get("attempts", 6), state.get("max_attempts", 6)),
        font=('Courier', 12),
        justify='left'
    )
    
    hangman_label.pack(side='left', padx=(0,12))

    right = tk.Frame(top)
    right.pack(side='left', fill='y')

    label_word = tk.Label(right, text=" ".join(state['lines']), font=('Arial', 14))
    label_word.pack(pady=10)

    entry = tk.Entry(right, font=('Arial', 14), width=5, justify='center')
    entry.pack(pady=10)
    entry.focus_set()

    attempts_label = tk.Label(right, text=f"Attempts: {state['attempts']}", font=('Arial', 12))
    attempts_label.pack()

    wrong_label = tk.Label(right, text="WRONG LETTERS: -", font=('Arial', 12), wraplength=300, justify='left')
    wrong_label.pack(pady=5)

    button_try = tk.Button(
        right,
        text="TRY",
        command=lambda: on_submit(entry, label_word, attempts_label, wrong_label,button_try)
        )
    button_try.pack(pady=5)

    button_reset = tk.Button(
        right,
        text="RESET",
        command=lambda: on_reset(entry, label_word, attempts_label, wrong_label, button_try)
        )
    button_reset.pack(pady=5)

    window.bind('<Return>', lambda e: button_try.invoke())


    def update_visuals():
        try:
            label_word.config(text=" ".join(state.get("lines", [])))

            attempts_label.config(text=f"Attempts: {state.get('attempts', 0)}")
            wrong = state.get("wrong", [])
            wrong_label.config(text="WRONG LETTERS: " + (", ".join(wrong) if wrong else "-"))

            max_att = state.get("max_attempts", 6)
            attempts_left = state.get('attempts', max_att)
            hangman_label.config(text=chose_hangman_stage(attempts_left, max_att))

            if "_" not in state.get('lines', []) or state.get('attempts', 1) <= 0:
                entry.config(state='disabled')
                button_try.config(state='disabled')
            else:
                entry.config(state='normal')
                button_try.config(state='normal')
        except:
            pass

        
    def submit_wrapper():
        #on_submit atualiza o state e labels que vc ja tinha.
        on_submit(entry, label_word, attempts_label, wrong_label, button_try)
        #garante que o hangman e demais labels estejam sincronizados
        update_visuals()

    
    def reset_wrapper():
        on_reset(entry, label_word, attempts_label, wrong_label, button_try)
        update_visuals()


    button_try.config(command=submit_wrapper)
    button_reset.config(command=reset_wrapper)

    update_visuals()

    return window, entry, label_word, attempts_label, wrong_label, button_try, button_reset
