import tkinter as tk
from PIL import Image, ImageTk
from word import words
import random

# ---------------- SETUP ----------------
window = tk.Tk()
window.title("Hangman")
window.geometry("600x600")

canvas = tk.Canvas(window, width=600, height=600)
canvas.pack(fill="both", expand=True)

# ---------------- IMAGES ----------------
hangman_files = [
    "base.png",       # starting empty stage
    "head.png",
    "body.png",
    "left hand.png",
    "right hand.png",
    "left leg.png",
    "right leg.png"   # final stage
]

# load images using PIL
hangman_images = [ImageTk.PhotoImage(Image.open(f)) for f in hangman_files]

# show initial image (base)
hangman_img = canvas.create_image(300, 200, image=hangman_images[0])

# ---------------- GAME VARIABLES ----------------
word = random.choice(words)
display = ["_"] * len(word)
guessed_letters = []
tries = 0
buttons = []

# text elements
word_text = canvas.create_text(300, 400, text=" ".join(display), font=("Arial", 24))
info_text = canvas.create_text(300, 450, text="Guess a letter", font=("Arial", 14))

# ---------------- FUNCTIONS ----------------
def update_display():
    canvas.itemconfig(word_text, text=" ".join(display))

def update_hangman():
    canvas.itemconfig(hangman_img, image=hangman_images[tries])

def check_guess(letter):
    global tries
    if letter in guessed_letters:
        canvas.itemconfig(info_text, text="Already guessed 😏")
        return

    guessed_letters.append(letter)
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
        canvas.itemconfig(info_text, text="Nice 😎")
    else:
        tries += 1
        canvas.itemconfig(info_text, text="Wrong 😵")
        update_hangman()

    update_display()
    check_game_over()

def check_game_over():
    if "_" not in display:
        canvas.itemconfig(info_text, text=f"🎉 You won! Word: {word} 😏")
        disable_buttons()
    elif tries == len(hangman_images) - 1:
        canvas.itemconfig(info_text, text=f"💀 You lost! Word: {word} 😅")
        disable_buttons()

def disable_buttons():
    for b in buttons:
        b.config(state="disabled")

def restart_game():
    global word, display, guessed_letters, tries
    word = random.choice(words)
    display = ["_"] * len(word)
    guessed_letters = []
    tries = 0
    update_display()
    canvas.itemconfig(hangman_img, image=hangman_images[0])
    canvas.itemconfig(info_text, text="Guess a letter")
    for b in buttons:
        b.config(state="normal")

# ---------------- LETTER BUTTONS ----------------
alphabet = "abcdefghijklmnopqrstuvwxyz"
x, y = 50, 500
for i, letter in enumerate(alphabet):
    btn = tk.Button(window, text=letter, width=3,
                    command=lambda l=letter: check_guess(l))
    canvas.create_window(x, y, window=btn)
    buttons.append(btn)
    x += 40
    if (i + 1) % 10 == 0:
        x = 50
        y += 40

# ---------------- RESTART BUTTON ----------------
restart_btn = tk.Button(window, text="Restart", width=10, command=restart_game, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
canvas.create_window(500, 550, window=restart_btn)

# ---------------- RUN ----------------
window.mainloop()