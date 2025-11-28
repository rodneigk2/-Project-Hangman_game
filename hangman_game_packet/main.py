from game_logic import create_state, process_guess
from ui import build_ui
from tkinter import messagebox

state = create_state("batata") ###################################

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
    
    if result == "hit":
        pass
    if result == "miss":
        pass

    label_word.config(text=" ".join(state["lines"]))
    attempts_label.config(text=f"Attempts: {state['attempts']}")

    if state["wrong"]:
        wrong_label.config(text=("Wrong Letters: " + ", ".join(state['wrong'])))
    
    if result == "You win":
        messagebox.showinfo("Victory!", f"The word was: {state["word"]}")
        button.config(state="disabled")
        return
    
    if result == "You lose": 
        messagebox.showinfo("Defeat!", f"The word was: {state["word"]}")
        button.config(state="disabled")
        return

window = build_ui(state, handle_submit)
window.mainloop()