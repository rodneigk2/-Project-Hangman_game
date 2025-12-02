from game_logic import create_state, process_guess
from ui import build_ui
from tkinter import messagebox

state = create_state("rato torto")

def _get_original_word_from_state(state):
    return state.get('original_word', state.get('word'))

def handle_submit(entry, label_word, attempts_label, wrong_label, button):
    letter = entry.get()
    entry.delete(0, 'end')

    result = process_guess(state, letter)

    if result == "Empty":
        return
    
    if result == "Enter only one letter":
        messagebox.showinfo("Warning!", "Entry only one letter")
        return
    
    if result == "Enter only letters":
        messagebox.showinfo("Warning!", "Entry only letters")
        return
    
    if result == "Repeated Entry":
        messagebox.showinfo("Warning!", "You've already tried this letter!")
        return

    label_word.config(text=" ".join(state["lines"]))
    attempts_label.config(text=f"Attempts: {state['attempts']}")

    if state["wrong"]:
        wrong_label.config(text="Wrong Letters: " + ", ".join(state["wrong"]))

    if result == "You win":
        messagebox.showinfo("Victory!", f"The word was: {_get_original_word_from_state}")
        button.config(state="disabled")
        entry.config(state="disabled")
        return
    
    if result == "You lose":
        messagebox.showinfo("Defeat!", f"The word was: {state['word']}")
        button.config(state="disabled")
        return


def on_reset(entry, label_word, attempts_label, wrong_label, button_try):
    original = _get_original_word_from_state(state)
    new_state = create_state(state["word"], max_attempts=state.get("max_attempts", 6))
    
    state.clear()
    state.update(new_state)

    entry.delete(0, 'end')
    entry.focus_set()

    label_word.config(text=" ".join(state["lines"]))
    attempts_label.config(text=f"Attempts: {state['attempts']}")
    wrong_label.config(text="WRONG LETTERS: -")

    button_try.config(state="normal")


window, entry, label_word, attempts_label, wrong_label, button_try, button_reset = \
    build_ui(state, handle_submit, on_reset)

window.mainloop()
