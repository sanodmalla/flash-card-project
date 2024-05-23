from tkinter import *
import pandas
import random

# ----------------------------- BUTTONS WORKINGS -------------------------------

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_french = current_card["French"]
    canvas.itemconfig(title, text="FRENCH", fill="black")
    canvas.itemconfig(front_image, image=card_front)
    canvas.itemconfig(word, text=current_french, fill="black")
    flip_timer = flip_timer = window.after(3000, func=flip_card)


def remove_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()


def flip_card():
    canvas.itemconfig(front_image, image=card_back)
    canvas.itemconfig(title, text="ENGLISH", fill="white")
    current_english = current_card["English"]
    canvas.itemconfig(word, text=current_english, fill="white")

# ------------------------------------ UI --------------------------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FLASHY")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
front_image = canvas.create_image(400, 263, image=card_front)
card_back = PhotoImage(file="images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text="", font=('Arial', 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

right_button = Button(image=right, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)



next_card()




window.mainloop()