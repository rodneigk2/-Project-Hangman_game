#Project Hangman_Game

#Password 
pass_word = 'apple'
lines_word = ['_'] * len(pass_word)

#Validate function
def letter_validate():
    letter = entrace.get()
    entrace.delete(0, tk.END)

    for index, char in enumerate(pass_word):
        if char == letter:
            lines_word[index] = char
    label_word.config(text=" ".join(lines_word))
    print(letter)

#Window created
import tkinter as tk

window = tk.Tk()
window.title('HANGMAN GAME')
window.geometry('400x300')

tk.Label(window, text='Hangman Game', font=("Arial", 14)).pack()

#Adding password in the window
label_word = tk.Label(window, text=" ".join(lines_word), font=("Arial", 20))
label_word.pack(pady=10)

#User entrace
entrace = tk.Entry(window, font=("Arial", 14),  width=5)
entrace.pack(pady=10) 

#Button creat
tk.Button(window, text="Try", command=letter_validate).pack(pady=5)

window.mainloop()
