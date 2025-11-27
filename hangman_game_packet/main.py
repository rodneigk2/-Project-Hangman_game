from game_logic import crate_state, process_guess
from ui import build_ui
from tkinter import messagebox

state = crate_state("ana piroca".replace(' ', '')) ###################################
def handle_submit(entry, label_word, attempts_label, wrong_label, button):
    letter = entry.get()
    entry.delete(0, 'end')

    result = process_guess(state, letter)

    label_word.config(text=" ".join(state["lines"]))
    attempts_label.config(text=f"Attempts: {state['attempts']}")

    if state["wrong"]:
        wrong_label.config(text=("Wrong Letters: " + ", ".join(state["wrong"])))

    if result == "Empty":
        return
    
    if result == "Invalid entry":
        messagebox.showinfo("Warning!", "Entry only one letter")
    
    if result == "Repeated Entry":
        messagebox.showinfo("Warning!", "You've already tried this letter!")
    
    
    if result == "You win":
        messagebox.showinfo("Victory!", f"The word was: {state["word"]}")
        button.config(state="disabled")

    if result == "You lose": 
        messagebox.showinfo("Defeat!", f"The word was: {state["word"]}")
        button.config(state="disabled")

window = build_ui(state, handle_submit)
window.mainloop()