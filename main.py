#Project Hangman_Game
import tkinter as tk
from tkinter import messagebox

#Password 
pass_word = 'apple'
lines_word = ['_'] * len(pass_word)

#Validate function
def letter_validate():
    global attempts
    letter = entrace.get().lower().strip()
    entrace.delete(0, tk.END)

    #Basic validations
    if not letter:
        messagebox.showinfo("Warning", "Type a letter.")
        return
    
    if len(letter) != 1 or not letter.isalpha():
        messagebox.showinfo("Warning", "Type only letters.")
        return
    
    #Check if you entered a repeated incorrect letter.
    if letter in wrong_letters:
        messagebox.showinfo("Warning", "Letters already attempted")
        return
    
    #Validates if a correct letter is repeated.
    if letter in lines_word:
        messagebox.showinfo("Warning", "Letters already attempted")
        return

    #Update the errors
    hit = False
    for index, char in enumerate(pass_word):
        if char == letter:
            lines_word[index] = char
            hit = True

    if hit:
        label_word.config(text=' '.join(lines_word))
    else:
        #Adds a wrong letter   
        attempts -= 1
        wrong_letters.append(letter)
        attempts_label.config(text=f"Attempts: {attempts}")
        wrong_label.config(text="Wrong letters: " + ", ".join(wrong_letters))

    #Check if you have finished all attempts.
    if attempts <= 0:
        messagebox.showinfo("Game over", f"You lose! the answer was: {pass_word}")
        button_try.config(state='disabled')
        return
    
    #Check if you win
    if "_" not in lines_word:
        messagebox.showinfo("Victory", f"You win! the answer was: {pass_word}")
        button_try.config(state='disabled')
        return

#Window created
window = tk.Tk()
window.title('HANGMAN GAME')
window.geometry('400x300')

tk.Label(window, text="Hangman Game", font=("Arial", 14)).pack()

#Adding password in the window
label_word = tk.Label(window, text=" ".join(lines_word), font=("Arial", 20))
label_word.pack(pady=10)

#User entrace
entrace = tk.Entry(window, font=("Arial", 14),  width=5)
entrace.pack(pady=10) 

#Attempts command
max_attempts = 6
attempts = max_attempts
wrong_letters = []

#
attempts_label = tk.Label(window, text=f"ATTEMPTS: {attempts}", font=("Arial", 12))
attempts_label.pack()

wrong_label = tk.Label(window, text="Wrong letters", font=("Arial", 12), wraplength=350, justify="left")
wrong_label.pack(pady=5)

#Button creat
button_try = tk.Button(window, text="Try", command=letter_validate)
button_try.pack(pady=5)

window.bind('<Return>', lambda e: letter_validate())

window.mainloop()
