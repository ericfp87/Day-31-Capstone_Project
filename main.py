from tkinter import *
import pandas
import random




BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
#Flip the Cards!

def flip_cards():

    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")



#New Flash Cards
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, flip_cards)



# UI
window = Tk()
window.title("Capstone")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, )

flip_timer = window.after(3000, flip_cards)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file=".\images\card_front.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_back_img = PhotoImage(file="images/card_back.png")

canvas.grid(row=0, column=0, columnspan=2)

# Labels

title_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="Title")
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="Word")


# Buttons

right_image = PhotoImage(file=".\images\Right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file=".\images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)



next_card()

window.mainloop()
